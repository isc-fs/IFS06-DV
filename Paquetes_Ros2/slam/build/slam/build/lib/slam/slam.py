import sys
import os
import time
import numpy
import cv2 as cv

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

from slam.cone_detection import *

class Cone_Detection(Node):

    def __init__(self):
        super().__init__('Cone_Detection')

        self.subscription = self.create_subscription(
            PointCloud2,
            'cloud_in',
            self.listener_callback,10)
        self.subscription

    def listener_callback(self, msg):
        points = parse_lidarData(numpy.asarray(msg.data))
        print("point 0  X: %f  Y: %f  Z: %f" % (points[0][0], points[0][1], points[0][2]))
        #print(len(data)/3)
        #print(final_cone_result_rt())
        #print(len(msg.data))
        #dfasf
        #self.publisher_Laser.publish(laser)

def parse_lidarData(self, point_cloud):
    """
    Takes an array of float points and converts it into an array with 3-item arrays representing x, y and z
    """
    points = numpy.array(point_cloud, dtype=numpy.dtype('f4'))
    return numpy.reshape(points, (int(points.shape[0]/3), 3))

def cone_detection(args=None):
    rclpy.init(args=args)

    cone = Cone_Detection()
    rclpy.spin(cone)