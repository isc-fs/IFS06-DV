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

from math import atan2, pi, sqrt

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
#import sklearn

def unit_vector(vector):
    return vector / numpy.linalg.norm(vector)

def angle(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return numpy.arccos(numpy.clip(numpy.dot(v1_u, v2_u), -1.0, 1.0))

millis = lambda: int(round(time.time() * 1000))

def wrap_to_pi(angle: float) -> float:  # in rads
    return (angle + pi) % (2 * pi) - pi

class Control(Node):
    def __init__(self):
        super().__init__('Control')
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

        #Vars
        self.v=0
        self.t_ant=0
        self.r_ant=0
        self.v_lat=0
        self.lookahead=3.0

    def listener_callback_v(self,msg):
        self.v=msg.twist.twist.linear.x

    def listener_callback(self,msg):
        self.path=msg

    def listener_callback_odom(self,msg):
        #msg=Odometry()
        self.v_lat=msg.twist.twist.linear.y

    def timer_callback(self):
        comando=ControlCommand()

        ###Control velocidad###
        comando.throttle=(self.v-7)*(-0.1)  #v_traget=2m/s
        comando.brake=0.0
        #print(self.v)

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

        target=self.get_target(posicion_cg)
        if target==-1:
            print("Publicando comando")
            self.publisher_comand.publish(comando)
            return
        
        comando.steering=self.comando_volate_cal(posicion_cg,target)
        
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

        ###Dos controladores P en cascada
        #setpoint=point_source.point.y*-1.8
        #comando.steering=(self.v_lat-setpoint)*-5.0
        
        #print((point_source.point.y,self.v_lat-setpoint))

        print("Publicando comando")
        
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
            # Distances are sorted, so once we get here just grab everything.
            indexes = indexes_raw[i:]
            distances = distances_raw[i:]
            break

        rvwp_dist = float("inf")
        rvwp_index = None
        for i in range(len(indexes)):
            index = indexes[i]
            p = path_xy[index]
            d = distances[i]

            # get angle to check if the point is in front of the car
            ang = self.angle(close, p)
            error = wrap_to_pi(pos[2] - ang)
            if numpy.pi / 2 > error > -numpy.pi / 2 and d < rvwp_dist:
                rvwp_dist = d
                rvwp_index = index

        if rvwp_index is None or rvwp_index == close_index:
            self.get_logger().warn("No se ha encontrado un punto a la distancia deseada")
            return -1
            """path_points_count = len(self.path) - 1
            fallback_point = close_index + self.fallback_path_points_offset
            if fallback_point > path_points_count:
                rvwp_index = abs(path_points_count - fallback_point)
            else:
                rvwp_index = fallback_point"""


        return (path_xy[rvwp_index][0],path_xy[rvwp_index][1])

    def angle(self,p1, p2) -> float:
        """
        Retrieve angle between two points
        * param p1: [x,y] coords of point 1
        * param p2: [x,y] coords of point 2
        * return: angle in rads
        """
        x_disp = p2[0] - p1[0]
        y_disp = p2[1] - p1[1]
        return atan2(y_disp, x_disp)
    
    def comando_volate_cal(self,pos,ref):
        des_heading_ang = self.angle(pos[:2], [ref[0], ref[1]])
        error = wrap_to_pi(pos[2] - des_heading_ang)
        angulo_deseado=numpy.rad2deg(error)
        print(angulo_deseado)
        steering = angulo_deseado * 1.8 #+angulo_deseado**3 *0.3
        steering=steering/25
        return steering

"""
Llamadas a Objetos para ROS2
"""

def control(args=None):
    rclpy.init(args=args)

    Laser_stam = Control()
    rclpy.spin(Laser_stam)