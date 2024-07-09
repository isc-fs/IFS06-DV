"""
========================
control.py (v1.0)
========================

Elaborado por Jaime Perez para el ISC
"""

import sys
import os
import time
import numpy
import cv2 as cv

from math import cos, sin

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy

from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped

from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray

from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Pose 
from geometry_msgs.msg import TwistWithCovarianceStamped

from sensor_msgs.msg import PointCloud2
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
import sensor_msgs.msg as sensor_msgs
import std_msgs.msg as std_msgs

from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from tf2_geometry_msgs import do_transform_point
from geometry_msgs.msg import Point
import geometry_msgs

from fs_msgs.msg import ControlCommand
from fs_msgs.srv import Reset

from transforms3d.euler import quat2euler

from scipy import interpolate
from sklearn.neighbors import KDTree
from control.utils import *

class Control(Node):
    def __init__(self):
        super().__init__('Control')
        self.init_params()
        #Publicar
        self.publisher_comand = self.create_publisher(ControlCommand, '/control_command',10)
        self.publisher_target = self.create_publisher(Marker, '/debug/target_point',10)
        #Subscricion
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self) 

        self.subscription_azul = self.create_subscription(
            Path,
            'Path',
            self.listener_callback,
            10)
        self.path=Path()
        
        self.subscription_v = self.create_subscription(
            TwistWithCovarianceStamped,
            'gss',
            self.listener_callback_v,
            10)
        
        self.subscription_posicion = self.create_subscription(
            Odometry,
            '/testing_only/odom',              ##Mensaje de Odometria---Mas adelante cambiar a estimacion VREL
            self.listener_callback_odom,
            10)

        #Timer
        self.timer = self.create_timer(1.0/40, self.timer_callback)   #Ejecutar a 40Hz (como minimo)

        self.v=0
        self.derv_ang=Derivada()
        self.derv_vel=Derivada()

    def init_params(self):
        self.declare_parameter("Kp_ang", 1.5)
        self.declare_parameter("Kd_ang", 1)           ###Esta ganacia aplifican ruido. Poner a 0 durante pruebas de odom
        self.declare_parameter("lookahead", 3.0)
        self.declare_parameter("max_steering_ang", 25.0)

        self.declare_parameter("Kp_vel", 0.1)
        self.declare_parameter("Kd_vel", 0.03)           ###Esta ganacia aplifican ruido. Poner a 0 durante pruebas de odom
        self.declare_parameter("vel_max", 8.0)
        self.declare_parameter("vel_min", 4.0)

        self.Kp_ang = self.get_parameter("Kp_ang").value
        self.Kd_ang = self.get_parameter("Kd_ang").value
        self.Kp_vel = self.get_parameter("Kp_ang").value
        self.Kd_vel = self.get_parameter("Kd_ang").value
        self.lookahead= self.get_parameter("lookahead").value
        self.v_max=self.get_parameter("vel_max").value
        self.v_min=self.get_parameter("vel_min").value
        self.max_steering_ang=self.get_parameter("max_steering_ang").value

    def listener_callback_v(self,msg):
        self.v=msg.twist.twist.linear.x

    def listener_callback(self,msg):
        self.path=msg

    def listener_callback_odom(self,msg):
        #msg=Odometry()
        self.v_lat=msg.twist.twist.linear.y

    def timer_callback(self):
        comando=ControlCommand()

        ###Control steering###
        try:        ###Generar Objeto de transformada entre Odom y el coche
            t = self.tf_buffer.lookup_transform(
                'odom',
                'fsds/FSCar',
                rclpy.time.Time())    ###Revisar tiempo
        except TransformException as ex:
            print(ex)                   ##Error al optener TF
            return
        
        try:        ###Generar Objeto de transformada entre Odom y el coche
            t_inv = self.tf_buffer.lookup_transform(
                'fsds/FSCar',
                'odom',
                rclpy.time.Time())    ###Revisar tiempo
        except TransformException as ex:
            print(ex)                   ##Error al optener TF
            return
        
        yaw = quat2euler(
            [
                t.transform.rotation.w,
                t.transform.rotation.x,
                t.transform.rotation.y,
                t.transform.rotation.z,
            ]
        )[2]
        
        posicion_cg=[t.transform.translation.x,t.transform.translation.y,yaw]
        posicion=self.get_pos_eje_delantero(posicion_cg)

        target=self.get_target(posicion)
        if target==-1:
            print("Publicando comando solo recto")
            comando.throttle=(self.v-self.v_min)*(-0.1)  #v_traget=2m/s
            self.publisher_comand.publish(comando)
            return
        
        #Publicar el target como marcador de rviz verde
        marker = Marker()
        marker.header.frame_id = "odom" ##El mapa esta en el sistema de referencia Odom no el coche
        marker.type = marker.CUBE
        marker.action = marker.ADD
        marker.scale.x = 0.5
        marker.scale.y = 0.5
        marker.scale.z = 0.5
        marker.color.a = 1.0
        marker.color.r = 0.0
        marker.color.g = 1.0
        marker.color.b = 0.0
        marker.pose.orientation.w = 1.0
        marker.pose.position.x = target[0]
        marker.pose.position.y = target[1]
        marker.pose.position.z = 0.0
        marker.id=0

        self.publisher_target.publish(marker)
        
        if len(self.path.poses)<1:
            comando.steering=0.0
            self.publisher_comand.publish(comando)
            return 0

        ang_volante=self.comando_volate_cal(posicion,target)
        comando.steering=ang_volante/self.max_steering_ang
        v_setpoiny=self.calc_velocidad(ang_volante)

        ###Control velocidad###
        v_error=-(self.v-v_setpoiny)
        if v_error>0:
            comp=v_error*self.Kp_vel+self.derv_vel.cal(v_error)*self.Kd_vel
            comando.throttle=min(comp,0.5)   #Limitar la aceleracion a a la mitad de la potencia
        else:   #La frenada se puede mejorar pero con la simulacion
            comando.brake=min(v_error*(-0.1),0.3)  #Limitar la frenada para no bloquear
            pass
        
        self.publisher_comand.publish(comando)

    def get_target(self,pos):

        path_xy = [[p.pose.position.x, p.pose.position.y] for p in self.path.poses]

        if len(path_xy)<1:
            return -1
        
        kdtree = KDTree(path_xy)
        close_index = kdtree.query([[pos[0], pos[1]]], return_distance=False)[0][0]
        close = path_xy[close_index] if close_index is not None else pos
        if close_index is None:
            self.get_logger().warn("No se puedo encontrar el punto mas cercano al coche")

        indexes_raw, distances_raw = kdtree.query_radius(
            [close], r=self.lookahead * 2, return_distance=True, sort_results=True
        )
        indexes_raw, distances_raw = indexes_raw[0], distances_raw[0]

        indexes, distances = [], []
        for i in range(len(indexes_raw)):
            if distances_raw[i] < self.lookahead:
                continue
            indexes = indexes_raw[i:]
            distances = distances_raw[i:]
            break

        dist = float("inf")
        index = None
        for i in range(len(indexes)):
            index = indexes[i]
            p = path_xy[index]
            d = distances[i]

            ang = angle(close, p)
            error = wrap_to_pi(pos[2] - ang)
            if numpy.pi / 2 > error > -numpy.pi / 2 and d < dist:
                dist = d
                index = index

        if index is None or index == close_index:
            self.get_logger().warn("No se ha encontrado un punto a la distancia deseada")
            index = close_index
            return -1


        return (path_xy[index][0],path_xy[index][1])
    
    def get_pos_eje_delantero(self, pos_cg):

        x_axle = pos_cg[0] + cos(pos_cg[2]) * 0.5
        y_axle = pos_cg[1] + sin(pos_cg[2]) * 0.5

        return [x_axle, y_axle, pos_cg[2]]
    
    def comando_volate_cal(self,pos,ref):
        ang_deseado = angle(pos[:2], [ref[0], ref[1]])
        error = wrap_to_pi(pos[2] - ang_deseado)
        ang_volante=numpy.rad2deg(error)
        steering = ang_volante * self.Kp_ang + self.derv_ang.cal(ang_volante)*self.Kd_ang
        self.t_ant=millis()
        self.a_ant=ang_volante
        return steering
     
    def calc_velocidad(self, ang_volante) -> float:
        vel = self.v_min + max((self.v_max - self.v_min) * (1 - (abs(ang_volante) / self.max_steering_ang) ** 2), 0)
        return vel

"""
Llamadas a Objetos para ROS2
"""

def control(args=None):
    rclpy.init(args=args)

    Laser_stam = Control()
    rclpy.spin(Laser_stam)