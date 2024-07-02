"""
========================
slam.py (v1.0)
========================

Elaborado por Jaime Perez para el ISC
Este nodo va separado del resto de slam para no cargar Numba para cada nodo

Contiene tres nodos:
1. Cone_Detection: Publica los resultados de final_cone_result_rt() este Nodo se puede mantener incendido y asi no hay que esperar
    a que compile cada vez que hay que probar. Numba tarda en optimizar el codigo y es tedioso hacerlo cada vez que se quiere probar.
"""

import sys
import os
import time
import numpy
import cv2 as cv
import math

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import PointCloud2
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
import sensor_msgs.msg as sensor_msgs
import std_msgs.msg as std_msgs

from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray

from slam.cone_detection import *

from fs_msgs.msg import Track, Cone

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

"""
Llamadas a Objetos para ROS2
"""
def cone_detection(args=None):
    rclpy.init(args=args)

    cone = Cone_Detection()
    rclpy.spin(cone)