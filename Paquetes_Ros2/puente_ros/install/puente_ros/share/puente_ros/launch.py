from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='puente_ros',
            namespace='',
            executable='puente_ros_odom',
            name='puente_ros_odom'
        ),
        Node(
            package='puente_ros',
            namespace='',
            executable='puente_ros_lidar',
            name='puente_ros_lidar'
        ),
        Node(
            package='puente_ros',
            namespace='',
            executable='puente_ros_camara',
            name='puente_ros_camara'
        )
    ])