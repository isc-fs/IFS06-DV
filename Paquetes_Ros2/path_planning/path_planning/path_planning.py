"""
========================
path_planning.py (v1.0)
========================

Elaborado por Jaime Perez para el ISC
Permite conectar el simulador FSDS a ROS2 mediante la API de Python.
Publica Odometria(/odom), TF coche-odom,
Datos de Lidar en formato nube de puntos(3D)(/cloud_in) y LaserScan(2D)(/scan)
La conversion de nube de puntos a Laser se hace con el paquete pointcloud-to-laserscan que se deve instalar(readme.md)
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

def frange(x, y, jump):
  while x < y:
    yield x
    x += jump

def gen_mark(x,y):
    mark=PoseStamped()
    mark.header.frame_id= "odom"

    mark.pose.position.x=x
    mark.pose.position.y=y
    mark.pose.position.z=0.0

    mark.pose.orientation.x=0.0
    mark.pose.orientation.y=0.0
    mark.pose.orientation.z=0.0
    mark.pose.orientation.w=0.0

    return mark

class Plan_Path(Node):
    def __init__(self):
        super().__init__('Plan_Path')
        #Publicar
        self.publisher_path = self.create_publisher(Path, 'Path',10)
        #Subscricion
        self.subscription_azul = self.create_subscription(
            Path,
            'Track_azul',
            self.listener_callback_azul,
            10)
        self.track_azul=Path()
        
        self.subscription_amarillo = self.create_subscription(
            Path,
            'Track_amarillo',
            self.listener_callback_amarillo,
            10)
        self.track_amarillo=Path()

    def listener_callback_azul(self, msg):
        self.track_azul=msg

    def listener_callback_amarillo(self, msg):
        self.track_amarillo=msg

        if len(self.track_azul.poses)>=2 and len(self.track_amarillo.poses)>=2:
            len_min=min((len(self.track_azul.poses),len(self.track_amarillo.poses)))

            puntos_x=[]
            puntos_y=[]
            for i in range(len_min):
                x=(self.track_azul.poses[i].pose.position.x+self.track_amarillo.poses[i].pose.position.x)/2
                y=(self.track_azul.poses[i].pose.position.y+self.track_amarillo.poses[i].pose.position.y)/2

                puntos_x.append(x)
                puntos_y.append(y)
    
            try:  ##Intentar interpolar con splines
                tck,a = interpolate.splprep([puntos_x,puntos_y],s=0.0,k=2)  #s=0 para forzar a que la curva pase por los puntos
                xnew,ynew= interpolate.splev(numpy.linspace(0,1,50),tck)
            except:
                print("error")
                return

            track=Path()
            track.header.frame_id= "odom"
            for (i,x) in enumerate(xnew):
                track.poses.append(gen_mark(x,ynew[i]))

            self.publisher_path.publish(track)

class Reser_server(Node):

    def __init__(self):
        super().__init__('Servicio_reset')
        self.cli = self.create_client(Reset, 'reset')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('El sevicio no esta disponible')
        self.req = Reset.Request()

    def send_request(self):
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

"""
Llamadas a Objetos para ROS2
"""

def plan_path(args=None):
    rclpy.init(args=args)

    Laser_stam = Plan_Path()
    rclpy.spin(Laser_stam)

def reiniciar(args=None):
    rclpy.init(args=args)

    minimal_client = Reser_server()
    minimal_client.send_request()
    minimal_client.destroy_node()
    rclpy.shutdown()


