"""
========================
coche_urdf.py (v1.0)
========================

Elaborado por Jaime Perez para el ISC

Para mostrar un modelo animado del coche es necesario publicar una serie de link con meshes asociados y unas trafsformadas de cada una de estos meshes.
En ros si se publican tf dinamicas desde distintos nodos estas se pueden desincronizar lo cual se manifiesta como vibraciones en las juntas entre las piezas del coche.
Por eso es necesario crear tranformadas estaticas he ir actualizando su posicion durante el tiempo de animacion.
robot_state_publisher se encarga de publicar las cordenadas a la ruedas y este programa de actualizar a 10Hz el angulo de las tf de las ruedas delanteras.
Esta implementado de esta manera para que la animacion sea suave pero las trasnformadas de este modulo no se pueden usar para calculos.
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

from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from fs_msgs.msg import ControlCommand

from tf2_ros import TransformBroadcaster
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster
from geometry_msgs.msg import TransformStamped

from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion

def euler_to_quaternion(yaw, pitch, roll):

        qx = numpy.sin(roll/2) * numpy.cos(pitch/2) * numpy.cos(yaw/2) - numpy.cos(roll/2) * numpy.sin(pitch/2) * numpy.sin(yaw/2)
        qy = numpy.cos(roll/2) * numpy.sin(pitch/2) * numpy.cos(yaw/2) + numpy.sin(roll/2) * numpy.cos(pitch/2) * numpy.sin(yaw/2)
        qz = numpy.cos(roll/2) * numpy.cos(pitch/2) * numpy.sin(yaw/2) - numpy.sin(roll/2) * numpy.sin(pitch/2) * numpy.cos(yaw/2)
        qw = numpy.cos(roll/2) * numpy.cos(pitch/2) * numpy.cos(yaw/2) + numpy.sin(roll/2) * numpy.sin(pitch/2) * numpy.sin(yaw/2)

        return [qx, qy, qz, qw]

class joint_states(Node):
    def __init__(self):
        super().__init__('joint_states')
        #Publicar
        self.publisher_comand = self.create_publisher(JointState, '/joint_states_t',10)
        self.tf_broadcaster = StaticTransformBroadcaster(self)

        #Subscricion
        self.subscription_azul = self.create_subscription(
            ControlCommand,
            '/control_command',
            self.listener_callback,
            10)
        
        self.p=0.0

    def listener_callback(self,control_msg):
        s=control_msg.steering*25
        if s>25:
             s=25
        elif s<-25:
             s=-25

        self.p=self.p*0.8+s*0.2  #Suavizar movimiento de ruedas

        t = TransformStamped()

        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'left_steering_hinge'
        t.child_frame_id = 'left_front_wheel'

        t.transform.translation.x = 0.0
        t.transform.translation.y = 0.0 
        t.transform.translation.z = 0.0

        rot = euler_to_quaternion(numpy.deg2rad(self.p),0,0)
        t.transform.rotation.x = rot[0]
        t.transform.rotation.y = rot[1]
        t.transform.rotation.z = rot[2]
        t.transform.rotation.w = rot[3]

        self.tf_broadcaster.sendTransform(t)

        t = TransformStamped()

        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'right_steering_hinge'
        t.child_frame_id = 'right_front_wheel'

        t.transform.translation.x = 0.0
        t.transform.translation.y = 0.0 
        t.transform.translation.z = 0.0

        rot = euler_to_quaternion(numpy.deg2rad(-self.p),0,0)
        t.transform.rotation.x = rot[0]
        t.transform.rotation.y = rot[1]
        t.transform.rotation.z = rot[2]
        t.transform.rotation.w = rot[3]

        self.tf_broadcaster.sendTransform(t)
        
        time.sleep(0.1) #Limitar actualizaciones a 10Hz

"""
Llamadas a Objetos para ROS2
"""

def publicar_joint_state(args=None):
    rclpy.init(args=args)

    joint_state = joint_states()
    rclpy.spin(joint_state)