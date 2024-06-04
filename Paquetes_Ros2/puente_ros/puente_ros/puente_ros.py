import sys
import os
import time
import numpy
import cv2 as cv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import puente_ros.fsds as fsds

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from sensor_msgs.msg import CameraInfo
from cv_bridge import CvBridge

from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped

from sensor_msgs.msg import PointCloud2
from nav_msgs.msg import Odometry
import sensor_msgs.msg as sensor_msgs
import std_msgs.msg as std_msgs


class Publicar_Lidar(Node):
    def __init__(self):
        super().__init__('Publicar_Lidar')
        self.publisher_ = self.create_publisher(PointCloud2, 'scan',10)

        client = fsds.FSDSClient()
        tiempo=0

        while(True):
            tiempo=time.time()
            msg = PointCloud2()

            try:
                lidardata = client.getLidarData(lidar_name = 'Lidar')

                msg = point_cloud(numpy.asarray(lidardata.point_cloud), 'base_frame')
                self.publisher_.publish(msg)

                self.get_logger().debug('Mesnaje enviado Lidar. Actualizaciones por seg:'+str(1/(time.time()-tiempo)))
            except:
                time.sleep(1)
                self.get_logger().error('Error Lidar')
                try:
                    client = fsds.FSDSClient()
                except:
                    pass

def point_cloud(points, parent_frame):
    #Esto no se como funciona
    """ Creates a point cloud message.
    Args:
        points: Nx3 array of xyz positions.
        parent_frame: frame in which the point cloud is defined
    Returns:
        sensor_msgs/PointCloud2 message

    Code source:
        https://gist.github.com/pgorczak/5c717baa44479fa064eb8d33ea4587e0

    References:
        http://docs.ros.org/melodic/api/sensor_msgs/html/msg/PointCloud2.html
        http://docs.ros.org/melodic/api/sensor_msgs/html/msg/PointField.html
        http://docs.ros.org/melodic/api/std_msgs/html/msg/Header.html

    """
    # In a PointCloud2 message, the point cloud is stored as an byte 
    # array. In order to unpack it, we also include some parameters 
    # which desribes the size of each individual point.
    ros_dtype = sensor_msgs.PointField.FLOAT32
    dtype = numpy.float32
    itemsize = numpy.dtype(dtype).itemsize # A 32-bit float takes 4 bytes.

    data = points.astype(dtype).tobytes() 

    # The fields specify what the bytes represents. The first 4 bytes 
    # represents the x-coordinate, the next 4 the y-coordinate, etc.
    fields = [sensor_msgs.PointField(
        name=n, offset=i*itemsize, datatype=ros_dtype, count=1)
        for i, n in enumerate('xyz')]

    # The PointCloud2 message also has a header which specifies which 
    # coordinate frame it is represented in. 
    header = std_msgs.Header(frame_id=parent_frame)

    return sensor_msgs.PointCloud2(
        header=header,
        height=1, 
        width=(int)(points.shape[0]/3),
        is_dense=True,
        is_bigendian=False,
        fields=fields,
        point_step=(itemsize * 3), # Every point consists of three float32s.
        row_step=(itemsize * 3 * points.shape[0]),
        data=data
    )

class Publicar_Camara(Node):
    def __init__(self):
        super().__init__('Publicar_Camara')
        self.publisher_ = self.create_publisher(Image, 'camara', 10)
        self.publisher_info = self.create_publisher(CameraInfo, 'camera_info', 10)

        client = fsds.FSDSClient()
        self.br = CvBridge()
        tiempo=0

        while(True):
            tiempo=time.time()
            try:
                [image] = client.simGetImages([fsds.ImageRequest(camera_name = 'cam', image_type = fsds.ImageType.Scene, pixels_as_float = False, compress = True)], vehicle_name = 'FSCar')
                #print(time.time()-tiempo)
                x = numpy.fromstring(image.image_data_uint8, dtype='uint8')
                img = cv.imdecode(x, cv.IMREAD_UNCHANGED)
                #cv.imshow("imagedfdfan",img); 
                #if cv.waitKey(1) & 0xFF == ord('q'): 
                    #pass
                
                msg=self.br.cv2_to_imgmsg(img)
                msg.header.stamp=self.get_clock().now().to_msg()
                msg.header.frame_id='base_frame'

                self.publisher_.publish(msg)

                #if True:
                self.get_logger().debug('Publicando camara. FPS:'+str(1/(time.time()-tiempo)))
            except:
                time.sleep(1)
                self.get_logger().error('Error Camara')
                try:
                    client = fsds.FSDSClient()
                except:
                    pass


class Publicar_Odom(Node):
    def __init__(self):
        super().__init__('Publicar_Odom')
        self.publisher_ = self.create_publisher(Odometry, 'odom', 10)

        client = fsds.FSDSClient()
        self.tf_broadcaster = TransformBroadcaster(self)

        tiempo=0

        while(True):
            tiempo=time.time()
            msg = Odometry()
            t = TransformStamped()

            try:
                state = client.getCarState()

                #######TF#######

                t.header.stamp = self.get_clock().now().to_msg()
                t.header.frame_id = 'odom_frame'
                t.child_frame_id = 'base_frame'

                t.transform.translation.x = state.kinematics_estimated.position.x_val
                t.transform.translation.y = state.kinematics_estimated.position.y_val
                t.transform.translation.z = state.kinematics_estimated.position.z_val

                t.transform.rotation.x = state.kinematics_estimated.orientation.x_val
                t.transform.rotation.y = state.kinematics_estimated.orientation.y_val
                t.transform.rotation.z = state.kinematics_estimated.orientation.z_val
                t.transform.rotation.w = state.kinematics_estimated.orientation.w_val

                self.tf_broadcaster.sendTransform(t)

                #######ODOM#######

                msg.header.stamp = self.get_clock().now().to_msg()

                msg.header.frame_id='odom_frame'

                msg.pose.pose.position.x = state.kinematics_estimated.position.x_val
                msg.pose.pose.position.y = state.kinematics_estimated.position.y_val
                msg.pose.pose.position.z = state.kinematics_estimated.position.z_val

                msg.pose.pose.orientation.x = state.kinematics_estimated.orientation.x_val
                msg.pose.pose.orientation.y = state.kinematics_estimated.orientation.y_val
                msg.pose.pose.orientation.z = state.kinematics_estimated.orientation.z_val
                msg.pose.pose.orientation.w = state.kinematics_estimated.orientation.w_val


                self.publisher_.publish(msg)
                self.get_logger().debug('Mesnaje enviado Odom')
            except:
                time.sleep(1)
                self.get_logger().error('Error Odom')
                try:
                    client = fsds.FSDSClient()
                except:
                    pass

def lidar(args=None):
    rclpy.init(args=args)

    Publicar_lidar = Publicar_Lidar()
    rclpy.spin(Publicar_lidar)

def odom(args=None):
    rclpy.init(args=args)

    Publicar_odom=Publicar_Odom()
    rclpy.spin(Publicar_odom)

def camara(args=None):
    rclpy.init(args=args)

    Publicar_camara=Publicar_Camara()
    rclpy.spin(Publicar_camara)

