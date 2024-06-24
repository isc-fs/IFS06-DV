"""
========================
puente_ros.launch.py (v1.0)
========================

Elaborado por Jaime Perez para el ISC
Lanza el puente del somulador FSDS con ROS
"""

import os

from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import LifecycleNode
from launch.substitutions import (AndSubstitution, LaunchConfiguration,NotSubstitution)
from launch.actions import (DeclareLaunchArgument, EmitEvent, LogInfo,RegisterEventHandler)
from launch_ros.actions import Node
from launch import actions

def generate_launch_description():
    log='info'  #Cambiar a debug para ver frecuencias de publicacion
    ld=LaunchDescription()

    ODOMETRIA = Node(   #ODOMETRIA
        package='puente_ros',
        namespace='',
        executable='puente_ros_TF',
        name='puente_ros_TF',
        arguments=['--ros-args', '--log-level', log]
    )

    LIDAR = Node( #LIDAR
        package='puente_ros',
        namespace='',
        executable='puente_ros_lidar',
        name='puente_ros_lidar',
        arguments=['--ros-args', '--log-level', log]
    )

    CAMARA = Node( #CAMARA
        package='puente_ros',
        namespace='',
        executable='puente_ros_camara',
        name='puente_ros_camara',
        arguments=['--ros-args', '--log-level', log]
    )

    LASER = Node( #CONVERSION POINTCLOUD A LASERSCAN
        package='pointcloud_to_laserscan', executable='pointcloud_to_laserscan_node',
        remappings=[('/cloud_in','/lidar/Lidar1',),         ##Remapeo de salidas del paqute de conversion de nuve de puntos a LaserScan para conseguir compativilidad con SlamToolBox
                   ('scan','scan')],
        name='pointcloud_to_laserscan'
        #arguments=['--ros-args', '--log-level', 'debug']
    )

    LASER_STAMP = Node( #AÑADIR TIME_STAMP A LASERSCAN   ##Si no se hace SlamToolBox no acepta los valores 
        package='puente_ros',
        namespace='',
        executable='puente_ros_laser',
        name='puente_ros_laser',
        arguments=['--ros-args', '--log-level', log]
    )

    SLAM_PARAM_FILE = DeclareLaunchArgument(  ##Configurar archivo de parametros SlamToolBox
        'slam_params_file',
        default_value='/home/jaime/Documents/IFS06-DV/Paquetes_Ros2/puente_ros/mapper_params_online_async.yaml'
      )  ##Ruta configuracion de Slam_Toolbox

    SLAM_TOOLBOX = LifecycleNode(
        parameters=[
          LaunchConfiguration('slam_params_file')
        ],
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        output='screen',
        namespace=''
    )

    #ld.add_action(CAMARA)
    ld.add_action(ODOMETRIA)
    #ld.add_action(LIDAR)
    #ld.add_action(LASER)
    #ld.add_action(LASER_STAMP)

    #ld.add_action(SLAM_PARAM_FILE)  ##SlamToolBox
    #ld.add_action(SLAM_TOOLBOX)

    return ld