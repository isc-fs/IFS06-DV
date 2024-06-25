"""
========================
puente_ros.launch.py (v1.0)
========================

Elaborado por Jaime Perez para el ISC
Lanza el modulo de SLAM
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

    CONE_DETECTION = Node(   #Detecion de conos
        package='slam',
        namespace='',
        executable='Cone_Detection',
        name='Cone_Detection',
        arguments=['--ros-args', '--log-level', log]
    )

    PUBLICAR_MAPA = Node( #Generar y publicar el mapa
        package='slam',
        namespace='',
        executable='Publicar_Mapa',
        name='Publicar_Mapa',
        arguments=['--ros-args', '--log-level', log]
    )

    PUBLICAR_TRACK = Node( #Genera MarkerArry de posicion real de los conos del circuito
        package='slam',
        namespace='',
        executable='Publicar_Track',
        name='Publicar_Track',
        arguments=['--ros-args', '--log-level', log]
    )

    ld.add_action(CONE_DETECTION)
    ld.add_action(PUBLICAR_MAPA)
    ld.add_action(PUBLICAR_TRACK)

    return ld