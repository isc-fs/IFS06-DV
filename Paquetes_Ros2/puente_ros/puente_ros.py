from launch import LaunchDescription
from launch_ros.actions import Node
from launch import actions

def generate_launch_description():
    log='info'  #Cambiar a debug para ver frecuencias de publicacion
    return LaunchDescription([
        Node(
            package='puente_ros',
            namespace='',
            executable='puente_ros_odom',
            name='puente_ros_odom',
            arguments=['--ros-args', '--log-level', log]
        ),
        Node(
            package='puente_ros',
            namespace='',
            executable='puente_ros_lidar',
            name='puente_ros_lidar',
            arguments=['--ros-args', '--log-level', log]
        ),
        Node(
            package='puente_ros',
            namespace='',
            executable='puente_ros_camara',
            name='puente_ros_camara',
            arguments=['--ros-args', '--log-level', log]
        )
    ])