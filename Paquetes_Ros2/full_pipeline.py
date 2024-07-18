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
from pathlib import Path

from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import LifecycleNode
from launch.substitutions import (AndSubstitution, LaunchConfiguration,NotSubstitution)
from launch.actions import (DeclareLaunchArgument, EmitEvent, LogInfo,RegisterEventHandler, IncludeLaunchDescription)
from launch import actions
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    log='info'  #Cambiar a debug para ver frecuencias de publicacion
    ld=LaunchDescription()

    RVIZ = Node(
        package='rviz2',
        namespace='',
        executable='rviz2',
        name='rviz2',
        arguments=['-d' + os.path.join(Path().absolute(), 'rviz_isc_config_v2.rviz')]
    )

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

    L_URDF=IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('coche_urdf'),"coche_urdf.launch.py")
        )
    )

    BENCHMARK_SLAM = Node(
        package='slam',
        namespace='',
        executable='BenchMark_Slam',
        name='BenchMark_Slam',
        prefix=["bash -c 'sleep 5; $0 $@' "],    ###Esperar 20seg a que numba compile
        arguments=['--ros-args', '--log-level', log]
    )

    ld.add_action(SLAM_PUBLICAR_TRACK)    #Para ver posicion real de los conos
    
    ld.add_action(RVIZ)
    ld.add_action(TF_ODOM_COCHE)
    ld.add_action(SLAM_CONE_DETECTION)
    ld.add_action(BENCHMARK_SLAM)
    ld.add_action(SLAM_PUBLICAR_MAPA)
    
    ld.add_action(PATH_PLANING)
    ld.add_action(CONTROL)
    ld.add_action(L_URDF)
    

    return ld