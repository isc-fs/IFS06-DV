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
from slam.mapa import *

from fs_msgs.msg import Track, Cone

from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener

class Cone_Detection(Node):
    """Publica los resultados de final_cone_result_rt() este Nodo se puede mantener incendido y asi no hay que esperar
    a que compile cada vez que hay que probar
    """
    def __init__(self):
        super().__init__('Cone_Detection')
        #Publicar
        self.publisher_MarkerArray = self.create_publisher(MarkerArray, 'Conos_raw',10)
        #Subscribir
        self.subscription = self.create_subscription(
            PointCloud2,
            '/lidar/Lidar1',
            self.listener_callback,10)
        
        self.subscription_odom = self.create_subscription(
            Odometry,
            '/testing_only/odom',
            self.listener_callback_odom,10)
        
        self.odom=Odometry()
        self.c=[]

    def listener_callback_odom(self, msg):
        self.odom=msg

    def listener_callback(self, msg):
        ###Wiki de FSDS
        points = numpy.array(np.frombuffer(msg.data, dtype=numpy.float32), dtype=numpy.dtype('f4'))
        point_cloud = numpy.reshape(points, (int(points.shape[0]/3), 3))

        conos=[]
        try:            ###A veces da error de division por cero. El try: es para evitar que crashe
            conos = final_cone_result_rt(point_cloud)  ###Consultar a Sergio
        except Exception as e:
            self.get_logger().error('error')
            pass
            
        self.get_logger().debug(str(len(conos)))
        markerArray = MarkerArray()

        """self.c.append([self.odom.header.stamp.sec,
            self.odom.header.stamp.nanosec,
            self.odom.pose.pose.position.x,
            self.odom.pose.pose.position.y,
            self.odom.pose.pose.orientation.x,
            self.odom.pose.pose.orientation.y,
            self.odom.pose.pose.orientation.z,
            self.odom.pose.pose.orientation.w,
            self.odom.twist.twist.linear.x,
            self.odom.twist.twist.linear.y,
            self.odom.twist.twist.angular.x,
            self.odom.twist.twist.angular.y,
            self.odom.twist.twist.angular.z,
            msg.header.stamp.sec,
            msg.header.stamp.nanosec])
        
        for i in range(20):
            if len(conos)>i:
                (a,b)=conos[i]
                self.c[len(self.c)-1].append(a)
                self.c[len(self.c)-1].append(b)
            else:
                self.c[len(self.c)-1].append(0.0)
                self.c[len(self.c)-1].append(0.0)
        np.savetxt('datos.txt',numpy.asarray(self.c), delimiter=',')"""

        ###Aprovechar el metodo MarkerArray() para mandar resultados de final_cone_result_rt()
        i=0
        for (a,b) in conos:
            self.get_logger().debug("x: "+str(a)+" Y: "+str(b))
            marker = Marker()
            marker.pose.position.x = a
            marker.pose.position.y = b
            marker.pose.position.z = 0.0

            ###Hacer compatible con RVIZ####
            marker.header.frame_id = "fsds/FSCar" ##El mapa esta en el sistema de referencia Odom no el coche
            marker.type = marker.CUBE
            if i==0:  ##En el pimer elemeto se le dice a RVIZ que elimine los registros. Mas info en Wiki RVIZ MarkerArray
                marker.action = 3  #ELIMINAR TODO 3
            else:
                marker.action = marker.ADD  #Añadir marcardo

            marker.header.stamp=msg.header.stamp
            marker.scale.x = 0.1
            marker.scale.y = 0.1
            marker.scale.z = 0.1
            marker.color.a = 1.0
            marker.color.r = 1.0
            marker.color.g = 0.0
            marker.color.b = 1.0
            marker.pose.orientation.w = 1.0
            marker.id=i
            i+=1
            ###Hacer compatible con RVIZ####

            markerArray.markers.append(marker)

        self.publisher_MarkerArray.publish(markerArray)

class Publicar_Mapa(Node):
    """Publica el mapa
    """
    def __init__(self):
        super().__init__('Publicar_Mapa')
        #Publicar
        self.publisher_MarkerArray = self.create_publisher(MarkerArray, 'Conos',10)

        #Subscripciones
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)   

        self.subscription = self.create_subscription(
            MarkerArray,
            'Conos_raw',
            self.listener_callback,10)

        #Iniciar calse Mapa
        self.mapa=Mapa()

    def listener_callback(self, msg):
        if len(msg.markers)==0: ###Si no se han detectado conos parar
            return
        
        markerArray = MarkerArray()

        ###Retroceder tiempo de medicion de lidar 30ms
        t_ofset=30000000
        if msg.markers[0].header.stamp.nanosec-t_ofset<0:
            msg.markers[0].header.stamp.sec=msg.markers[0].header.stamp.sec-1
            msg.markers[0].header.stamp.nanosec=msg.markers[0].header.stamp.nanosec-t_ofset+1000000000
        else:
            msg.markers[0].header.stamp.nanosec=msg.markers[0].header.stamp.nanosec-t_ofset

        try:        ###Generar Objeto de transformada entre Odom y el coche
            t = self.tf_buffer.lookup_transform(
                'odom',
                'fsds/FSCar',
                msg.markers[0].header.stamp) #Coger tiempo del escaneo para interpolar
        except TransformException as ex:
            return
        
        for mark in msg.markers:  ###Añadir conos que detectado final_cone_result_rt() a el mapa
            self.mapa.add_cono(mark.pose.position.x, mark.pose.position.y,t)

        self.mapa.actualizar_mapa()

        i=0
        for cono in self.mapa.conos:        ###Mostrar el mapa completo
            marker = Marker()
            marker.header.frame_id = "odom" ##El mapa esta en el sistema de referencia Odom no el coche
            marker.type = marker.CUBE
            if i==0:  ##En el pimer elemeto se le dice a RVIZ que elimine los registros. Mas info en Wiki RVIZ MarkerArray
                marker.action = 3  #ELIMINAR TODO 3
            else:
                marker.action = marker.ADD  #Añadir marcardo

            marker.scale.x = 0.1
            marker.scale.y = 0.1
            marker.scale.z = 0.1
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
            '/lidar/Lidar1',
            self.listener_callback,10)

    def listener_callback(self, msg):
        points = numpy.array(np.frombuffer(msg.data, dtype=numpy.float32), dtype=numpy.dtype('f4'))
        point_cloud = numpy.reshape(points, (int(points.shape[0]/3), 3))

        conos=[]
        try:
            conos = final_cone_result_rt(point_cloud)
        except:
            pass
            
        self.get_logger().error(str(len(conos)))
        laser = LaserScan()

        laser.header.stamp=msg.header.stamp
        t_ofset=30000000
        if laser.header.stamp.nanosec-t_ofset<0:
            laser.header.stamp.sec=laser.header.stamp.sec-1
            laser.header.stamp.nanosec=laser.header.stamp.nanosec-t_ofset+1000000000
        else:
            laser.header.stamp.nanosec=laser.header.stamp.nanosec-t_ofset

        laser.header.frame_id='fsds/FSCar'

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


class Publicar_Track(Node):
    def __init__(self):
        super().__init__('Publicar_Laser')
        #Publicar
        self.publisher_MarkerArray = self.create_publisher(MarkerArray, 'Track',10)
        #Subscripcion
        self.subscription = self.create_subscription(
            Track,
            '/testing_only/track',
            self.listener_callback,10)

    def listener_callback(self, msg):
        Cone_list = MarkerArray()

        i=0

        #c=[(cone.location.x,cone.location.y) for cone in msg.track]
        #np.savetxt('track.txt',numpy.asarray(c), delimiter=',')

        for cone in msg.track:

            marker = Marker()
            marker.header.frame_id = "odom" ##El mapa esta en el sistema de referencia Odom no el coche
            marker.type = marker.CUBE
            if i==0:  ##En el pimer elemeto se le dice a RVIZ que elimine los registros. Mas info en Wiki RVIZ MarkerArray
                marker.action = 3  #ELIMINAR TODO 3
            else:
                marker.action = marker.ADD  #Añadir marcardo

            marker.scale.x = 0.1
            marker.scale.y = 0.1
            marker.scale.z = 0.1
            marker.color.a = 1.0
            marker.color.r = 0.0
            marker.color.g = 1.0
            marker.color.b = 0.0
            marker.pose.orientation.w = 1.0
            marker.pose.position.x = cone.location.x
            marker.pose.position.y = cone.location.y
            marker.pose.position.z = 0.0
            marker.id=i
            i+=1

            Cone_list.markers.append(marker)

        self.publisher_MarkerArray.publish(Cone_list)
        print(len(Cone_list.markers))

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

def publicar_track(args=None):
    rclpy.init(args=args)

    nodo_laser = Publicar_Track()
    rclpy.spin(nodo_laser)