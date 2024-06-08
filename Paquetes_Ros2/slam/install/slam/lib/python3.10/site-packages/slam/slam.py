"""
========================
slam.py (v1.0)
========================

Elaborado por Jaime Perez para el ISC
Contiene las funciones para realizar el Slam.
Se ha decidido separar este codfio de la parte del puente_ros para simplificar el codigo y mejorar el paralelizacion.

Contiene tres nodos:
1. Cone_Detection: Publica los resultados de final_cone_result_rt() este Nodo se puede mantener incendido y asi no hay que esperar
    a que compile cada vez que hay que probar. Numba tarda en optimizar el codigo y es tedioso hacerlo cada vez que se quiere probar.

2. Publicar_Mapa: Se suscribe al nodo anterior y añade esos conos a un mapa de features (mapa.py-mas detelles). Luego publica el mapa
    entero con un MarkerArray a RVIZ.

3. Publicar_Laser(EXPERIMENTO): Pretende publicar como un escaneo de laser los reslutados de Cone_Detection. Para luego introducirlo en SlamToolBox
"""

import sys
import os
import time
import numpy
import cv2 as cv
import math

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy

from sensor_msgs.msg import Image
from sensor_msgs.msg import CameraInfo
from cv_bridge import CvBridge

from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped

from sensor_msgs.msg import PointCloud2
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
import sensor_msgs.msg as sensor_msgs
import std_msgs.msg as std_msgs

from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray

from slam.cone_detection import *
from slam.mapa import Mapa, Cono

from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener

class Cone_Detection(Node):
    """Publica los resultados de final_cone_result_rt() este Nodo se puede mantener incendido y asi no hay que esperar
    a que compile cada vez que hay que probar
    """
    def __init__(self):
        super().__init__('Cone_Detection')

        self.publisher_MarkerArray = self.create_publisher(MarkerArray, 'Conos_raw',10)

        self.subscription = self.create_subscription(
            PointCloud2,
            'cloud_in',
            self.listener_callback,10)
        self.subscription

    def listener_callback(self, msg):
        x=np.frombuffer(msg.data, dtype=numpy.float32)
        point_cloud = parse_lidarData(x)

        conos=[]
        try:            ###A veces da error de division por cero. El try: es para evitar que crashe
            conos = final_cone_result_rt(point_cloud)
        except:
            pass
            
        self.get_logger().debug(str(len(conos)))
        markerArray = MarkerArray()
        ###Aprovechar el metodo MarkerArray() pero no es compatible con RVIZ
        for (a,b) in conos:
            self.get_logger().debug("x: "+str(a)+" Y: "+str(b))
            marker = Marker()
            marker.pose.position.x = a
            marker.pose.position.y = b
            marker.pose.position.z = 0.0

            markerArray.markers.append(marker)

        self.publisher_MarkerArray.publish(markerArray)

def parse_lidarData(point_cloud):       ###Wiki de FSDS
    points = numpy.array(point_cloud, dtype=numpy.dtype('f4'))
    return numpy.reshape(points, (int(points.shape[0]/3), 3))

class Publicar_Mapa(Node):
    """Publica el mapa
    """
    def __init__(self):
        super().__init__('Publicar_Mapa')

        self.publisher_MarkerArray = self.create_publisher(MarkerArray, 'Conos',10)

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)   

        self.subscription = self.create_subscription(
            MarkerArray,
            'Conos_raw',
            self.listener_callback,10)
        self.subscription

        self.mapa=Mapa()

    def listener_callback(self, msg):
        markerArray = MarkerArray()
        try:        ###Generar Objeto de transformada entre Odom y el coche
            t = self.tf_buffer.lookup_transform(
                'odom',
                'base_footprint',
                rclpy.time.Time())
        except TransformException as ex:
            return
        
        for mark in msg.markers:  ###Añadir conos que detectado final_cone_result_rt() a el mapa
            self.mapa.add_cono(mark.pose.position.x, mark.pose.position.y,t)

        i=0
        for cono in self.mapa.conos:        ###Mostrar el mapa completo
            marker = Marker()
            marker.header.frame_id = "odom" ##El mapa esta en el sistema de referencia Odom no el coche
            marker.type = marker.CUBE
            if i==0:  ##En el pimer elemeto se le dice a RVIZ que elimine los registros. Mas info en Wiki RVIZ MarkerArray
                marker.action = 3  #ELIMINAR TODO 3
            else:
                marker.action = marker.ADD  #Añadir marcardo

            marker.scale.x = 0.5
            marker.scale.y = 0.5
            marker.scale.z = 0.5
            marker.color.a = 1.0
            marker.color.r = 1.0
            marker.color.g = 1.0
            marker.color.b = 0.0
            marker.pose.orientation.w = 1.0
            marker.pose.position.x = cono.x
            marker.pose.position.y = cono.y
            marker.pose.position.z = 0.0
            marker.id=i
            i+=1

            markerArray.markers.append(marker)

        self.publisher_MarkerArray.publish(markerArray)

class Publicar_Laser(Node):
    """Experimental
    """
    def __init__(self):
        super().__init__('Publicar_Laser')

        self.publisher_Laser = self.create_publisher(LaserScan, 'Laser_Conos',10)

        self.subscription = self.create_subscription(
            PointCloud2,
            'cloud_in',
            self.listener_callback,10)
        self.subscription

    def listener_callback(self, msg):
        x=np.frombuffer(msg.data, dtype=numpy.float32)
        point_cloud = parse_lidarData(x)

        conos=[]
        try:
            conos = final_cone_result_rt(point_cloud)
        except:
            pass
            
        self.get_logger().error(str(len(conos)))
        laser = LaserScan()

        laser.header.stamp=self.get_clock().now().to_msg()
        laser.header.frame_id='base_footprint'

        laser.angle_min=-math.pi
        laser.angle_max=math.pi
        laser.angle_increment=(math.pi*2)/360.0

        laser.range_min=0.0
        laser.range_max=float('inf')

        laser.scan_time=0.03333333507180214

        #self.get_logger().error(str(len(laser.ranges)))

        for i in range(361):
            laser.ranges.append(float('inf'))
        
        for (a,b) in conos:
            (a,b)=rect2polars(a,b)
            i=round(math.degrees(b))
            print(i)
            i+=180
            if(i<360 and i>0):
                laser.ranges[i]=a
        
        self.publisher_Laser.publish(laser)


"""
Llamadas a Objetos para ROS2
"""
def cone_detection(args=None):
    rclpy.init(args=args)

    cone = Cone_Detection()
    rclpy.spin(cone)

def publicar_mapa(args=None):
    rclpy.init(args=args)

    mapa = Publicar_Mapa()
    rclpy.spin(mapa)

def cone_laser(args=None):
    rclpy.init(args=args)

    nodo_laser = Publicar_Laser()
    rclpy.spin(nodo_laser)