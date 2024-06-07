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

from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray

from slam.cone_detection import *

class Cone_Detection(Node):

    def __init__(self):
        super().__init__('Cone_Detection')

        self.publisher_MarkerArray = self.create_publisher(MarkerArray, 'Conos',10)

        self.subscription = self.create_subscription(
            PointCloud2,
            'cloud_in',
            self.listener_callback,10)
        self.subscription

    def listener_callback(self, msg):
        x=np.frombuffer(msg.data, dtype=numpy.float32)
        point_cloud = parse_lidarData(x)

        conos=[]
        try:
            conos = final_cone_result_rt(point_cloud)
        except:
            pass
            
        self.get_logger().debug(str(len(conos)))
        markerArray = MarkerArray()
        i=0
        for (a,b) in conos:
            self.get_logger().debug("x: "+str(a)+" Y: "+str(b))
            marker = Marker()
            marker.header.frame_id = "/base_footprint"
            marker.type = marker.CUBE
            if i==0:
                marker.action = 3 #ELIMINAR TODO
            else:
                marker.action = marker.ADD
            marker.scale.x = 0.5
            marker.scale.y = 0.5
            marker.scale.z = 0.5
            marker.color.a = 1.0
            marker.color.r = 1.0
            marker.color.g = 1.0
            marker.color.b = 0.0
            marker.pose.orientation.w = 1.0
            marker.pose.position.x = a
            marker.pose.position.y = b
            marker.pose.position.z = 0.0
            marker.id=i
            i+=1

            markerArray.markers.append(marker)

        self.publisher_MarkerArray.publish(markerArray)

def parse_lidarData(point_cloud):
    points = numpy.array(point_cloud, dtype=numpy.dtype('f4'))
    return numpy.reshape(points, (int(points.shape[0]/3), 3))

def cone_detection(args=None):
    rclpy.init(args=args)

    cone = Cone_Detection()
    rclpy.spin(cone)