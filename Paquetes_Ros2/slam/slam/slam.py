"""
========================
slam.py (v1.0)
========================

Elaborado por Jaime Perez para el ISC
Contiene las funciones para realizar el Slam.
Se ha decidido separar este codfio de la parte del puente_ros para simplificar el codigo y mejorar el paralelizacion.

Contiene tres nodos:
1. Publicar_Mapa: Se suscribe al nodo anterior y añade esos conos a un mapa de features (mapa.py-mas detelles). Luego publica el mapa
    entero con un MarkerArray a RVIZ.

1. Publicar_Track: Publica la posicion real de los conos del track

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

from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped

from sensor_msgs.msg import PointCloud2
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
import sensor_msgs.msg as sensor_msgs
import std_msgs.msg as std_msgs

from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray

from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Pose

from slam.mapa import *

from fs_msgs.msg import Track, Cone
from fs_msgs.srv import Reset

from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener

class Publicar_Mapa(Node):
    """Publica el mapa
    """
    def __init__(self):
        super().__init__('Publicar_Mapa')
        #Publicar
        self.publisher_MarkerArray = self.create_publisher(MarkerArray, 'Conos',10)
        self.publisher_Path_azul = self.create_publisher(Path, 'Track_azul',10)
        self.publisher_Path_amarillo = self.create_publisher(Path, 'Track_amarillo',10)

        #Subscripciones
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)   

        self.subscription = self.create_subscription(
            MarkerArray,
            'Conos_raw',
            self.listener_callback,10)
        
        self.subscription = self.create_subscription(
            MarkerArray,
            'Track',
            self.listener_callback_track,10)
        self.track=[]
        
        #Servicio de reset
        self.srv = self.create_service(Reset, 'reset', self.reset_callback)

        #Iniciar calse Mapa
        self.mapa=Mapa()

    def reset_callback(self, request, response):
        self.mapa.conos=[]
        self.mapa.deteciones=[]
        self.get_logger().info('Reseteando Mapa')
        return response
    
    def listener_callback_track(self, msg):     ##Menchamrk
        for cone in msg.markers:
            self.track.append((cone.pose.position.x,cone.pose.position.y))
        self.mapa.track=self.track

    def listener_callback(self, msg):
        if len(msg.markers)==0: ###Si no se han detectado conos parar
            return

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
        
        try:        ###Generar Objeto de transformada entre coche y odom. Transformada inversa
            t_inv = self.tf_buffer.lookup_transform(
                'fsds/FSCar',
                'odom',
                msg.markers[0].header.stamp) #Coger tiempo del escaneo para interpolar
        except TransformException as ex:
            return
        
        for mark in msg.markers:  ###Añadir conos que detectado final_cone_result_rt() a el mapa
            self.mapa.add_detecion(mark.pose.position.x, mark.pose.position.y,t,t_inv)

        self.mapa.actualizar_mapa()
        self.mapa.generar_trazas(t,t_inv)
        
        markerArray = MarkerArray()

        ###Mostrar Conos con Marker Array###
        #Eliminar marcadores anterioires
        marker = Marker()
        marker.header.frame_id = "odom"
        marker.type = marker.CUBE
        marker.action = 3  #ELIMINAR TODO 3
        marker.id=0
        markerArray.markers.append(marker)

        for (i,cono) in enumerate(self.mapa.conos):        ###Mostrar el mapa completo
            marker = Marker()
            marker.header.frame_id = "odom" ##El mapa esta en el sistema de referencia Odom no el coche
            marker.type = marker.MESH_RESOURCE
            marker.action = marker.ADD  #Añadir marcardo

            ##Tamaño de m
            marker.scale.x = 1.0
            marker.scale.y = 1.0
            marker.scale.z = 1.0

            #Hay que incluir la referencia en setup.py para que colcon añada al ejecutable la carpeta de meches
            marker.mesh_resource='package://slam/meshes/any_small.dae'

            if cono.color=='ref':
                marker.color.r = 1.0
                marker.color.g = 1.0
                marker.color.b = 1.0
                marker.color.a = 1.0

            if cono.color=='cont':
                marker.color.r = 1.0
                marker.color.g = 0.0
                marker.color.b = 0.0
                marker.color.a = 1.0

            ##Color
            if cono.color=='Azul':
                marker.color.r = 0.0
                marker.color.g = 0.0
                marker.color.b = 1.0
                marker.color.a = 1.0
            elif cono.color=='Amarillo': #Amarillo
                marker.color.r = 1.0
                marker.color.g = 1.0
                marker.color.b = 0.0
                marker.color.a = 1.0

            elif cono.color=='ns': #No se sabe
                marker.color.r = 1.0
                marker.color.g = 1.0
                marker.color.b = 1.0
                marker.color.a = 1.0

            ##Posicion
            marker.pose.orientation.w = 1.0
            marker.pose.position.x = cono.x
            marker.pose.position.y = cono.y
            marker.pose.position.z = 0.0
            marker.id=i+1

            markerArray.markers.append(marker)

        self.publisher_MarkerArray.publish(markerArray)

        ###Mostrar Track###
        ###Azul###
        track=Path()
        track.header.frame_id= "odom"
        for (i,pose) in enumerate(self.mapa.track_azul):
            mark=PoseStamped()
            mark.header.frame_id= "odom"

            mark.pose.position.x=pose.x
            mark.pose.position.y=pose.y
            mark.pose.position.z=0.0

            mark.pose.orientation.x=0.0
            mark.pose.orientation.y=0.0
            mark.pose.orientation.z=0.0
            mark.pose.orientation.w=0.0

            track.poses.append(mark)

        self.publisher_Path_azul.publish(track)

        ###Amarillo###
        track=Path()
        track.header.frame_id= "odom"
        for (i,pose) in enumerate(self.mapa.track_amarillo):
            mark=PoseStamped()
            mark.header.frame_id= "odom"

            mark.pose.position.x=pose.x
            mark.pose.position.y=pose.y
            mark.pose.position.z=0.0

            mark.pose.orientation.x=0.0
            mark.pose.orientation.y=0.0
            mark.pose.orientation.z=0.0
            mark.pose.orientation.w=0.0

            track.poses.append(mark)

        self.publisher_Path_amarillo.publish(track)

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
        self.r_msg=Track()

        #Timer
        self.timer = self.create_timer(5, self.timer_callback)
    def listener_callback(self, msg):
        self.r_msg=msg

    def timer_callback(self):
        Cone_list = MarkerArray()
        i=0
        for cone in self.r_msg.track:

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

class BenchMark(Node):
    def __init__(self):
        super().__init__('BenchMark_Slam')

        self.subscription = self.create_subscription(
            MarkerArray,
            'Conos',
            self.listener_callback,10)
        self.len_conos=0
        
        self.subscription = self.create_subscription(
            MarkerArray,
            'Track',
            self.listener_callback_track,10)
        self.len_conos=0

    def listener_callback_track(self, msg):
        #Cone_list = MarkerArray()
        self.len_conos=len(msg.markers)
        
        """for cone in msg.track:
            cone.location.x
            cone.location.y"""

    def listener_callback(self, msg):
        #self.get_logger().info('n_detectados')
        #self.get_logger().info(str(len(msg.markers)))
        #self.get_logger().info('n_real')
        #self.get_logger().info(str(self.len_conos))
        pass

"""
Llamadas a Objetos para ROS2
"""

def publicar_mapa(args=None):
    rclpy.init(args=args)

    mapa = Publicar_Mapa()
    rclpy.spin(mapa)

def BenchMark_Slam(args=None):
    rclpy.init(args=args)

    BenchMark_slam = BenchMark()
    rclpy.spin(BenchMark_slam)

def publicar_track(args=None):
    rclpy.init(args=args)

    nodo_laser = Publicar_Track()
    rclpy.spin(nodo_laser)