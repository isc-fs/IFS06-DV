"""
========================
puente_ros.launch.py (v1.0)
========================

Elaborado por Jaime Perez para el ISC
Lanza todo el pipeline a excepcion del simulador y el puente y rviz
Se puede hacer con:
cd ~/Formula-Student-Driverless-Simulator
./FSDS.sh
source ~/Formula-Student-Driverless-Simulator/ros2/install/setup.sh
ros2 launch fsds_ros2_bridge fsds_ros2_bridge.launch.py
rviz2
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

    TF_ODOM_COCHE = Node(
        package='puente_ros',
        namespace='',
        executable='puente_ros_TF',
        name='puente_ros_TF',
        arguments=['--ros-args', '--log-level', log]
    )

    SLAM_CONE_DETECTION = Node(
        package='slam',
        namespace='',
        executable='Cone_Detection',
        name='Cone_Detection',
        arguments=['--ros-args', '--log-level', log]
    )

    SLAM_PUBLICAR_MAPA = Node(
        package='slam',
        namespace='',
        executable='Publicar_Mapa',
        name='Publicar_Mapa',
        arguments=['--ros-args', '--log-level', log]
    )

    SLAM_PUBLICAR_TRACK = Node(
        package='slam',
        namespace='',
        executable='Publicar_Track',
        name='Publicar_Track',
        arguments=['--ros-args', '--log-level', log]
    )

    PATH_PLANING = Node(
        package='path_planning',
        namespace='',
        executable='Plan_Path',
        name='path_planning',
        arguments=['--ros-args', '--log-level', log]
    )

    CONTROL = Node(
        package='control',
        namespace='',
        executable='Control',
        name='control',
        prefix=["bash -c 'sleep 20; $0 $@' "],    ###Esperar 20seg a que numba compile
        arguments=['--ros-args', '--log-level', log]
    )

    ld.add_action(TF_ODOM_COCHE)
    ld.add_action(SLAM_CONE_DETECTION)
    ld.add_action(SLAM_PUBLICAR_MAPA)
    #ld.add_action(SLAM_PUBLICAR_TRACK)    #Para ver posicion real de los conos
    ld.add_action(PATH_PLANING)
    ld.add_action(CONTROL)

    return ld