"""
========================
yolo.py (v1.0)
========================
"""

import sys
import os
import time
import numpy
import cv2
import math

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge

from yolo.yolo_model import YOLOModel

from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray

class YOLO(Node):
    """Publica el mapa
    """
    def __init__(self):
        super().__init__('Yolo')
        self.bridge = CvBridge()
        #Publicar
        self.publisher_Resultado = self.create_publisher(MarkerArray, 'Yolo_result',10)

        #Subscripciones  
        self.subscription = self.create_subscription(
            Image,
            '/fsds/cameracam1/image_color',
            self.listener_callback,10)
        
        #Setup Yolo
        path_weights = "weights/best.pt"  # Path to the YOLO model weights
        camera_parameters = {
            "width": 1280,
            "height": 720,
            "fov": 90,
        }

        # Cone dimensions in meters
        cone_dimensions = {
            "width": 0.228,
            "height": 0.325,
            "depth": 0.228,
        }

        # Initialize YOLOModel object
        self.model = YOLOModel(
            model_path=path_weights,
            camera_parameters=camera_parameters,
            cone_dimensions=cone_dimensions,
        )

    def listener_callback(self, msg):
        imagen = self.bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')

        prediciones = self.model.get_points(imagen)

        markerArray = MarkerArray()
        for (i,pred) in enumerate(prediciones):
            (a,b)=pred[0]

            marker = Marker()
            marker.pose.position.x = b  #Cambiar sistema de referecia para concordar con el del ros
            marker.pose.position.y = -a
            marker.pose.position.z = 0.0

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
            #print(i[0])
            #(x,y)=i[0]
            print(pred)  # Print the detected cone positions and types

            markerArray.markers.append(marker)

        self.publisher_Resultado.publish(markerArray)



"""
Llamadas a Objetos para ROS2
"""

def Yolo(args=None):
    rclpy.init(args=args)

    mapa = YOLO()
    rclpy.spin(mapa)