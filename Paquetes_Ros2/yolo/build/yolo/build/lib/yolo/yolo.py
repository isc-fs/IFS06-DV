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

class YOLO(Node):
    """Publica el mapa
    """
    def __init__(self):
        super().__init__('Yolo')
        self.bridge = CvBridge()
        #Publicar
        self.publisher_Resultado = self.create_publisher(Image, 'Resultado',10)

        #Subscripciones  
        self.subscription = self.create_subscription(
            Image,
            '/fsds/cameracam1/image_color',
            self.listener_callback,10)
        
        #Setup Yolo
        path_weights = "weights/best.pt"  # Path to the YOLO model weights
        camera_parameters = {
            "fx": 1000,
            "fy": 1000,
            "cx": 940,
            "cy": 740,
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

        pred = self.model.get_points(imagen)

        for i in pred:
            print(i)  # Print the detected cone positions and types



"""
Llamadas a Objetos para ROS2
"""

def Yolo(args=None):
    rclpy.init(args=args)

    mapa = YOLO()
    rclpy.spin(mapa)