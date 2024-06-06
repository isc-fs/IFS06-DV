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
        executable='puente_ros_odom',
        name='puente_ros_odom',
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
        remappings=[('scan_in', 'scan_in'),
                    ('scan','scan_pre')],
        name='pointcloud_to_laserscan'
    )

    LASER_STAMP = Node( #AÑADIR TIME_STAMP A LASERSCAN
        package='puente_ros',
        namespace='',
        executable='puente_ros_laser',
        name='puente_ros_laser',
        arguments=['--ros-args', '--log-level', log]
    )

    CONE = Node( #
        package='puente_ros',
        namespace='',
        executable='cone',
        name='cone',
        arguments=['--ros-args', '--log-level', log]
    )

    SLAM_PARAM_FILE = DeclareLaunchArgument(
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
    ld.add_action(LIDAR)
    ld.add_action(LASER)
    ld.add_action(LASER_STAMP)

    #ld.add_action(SLAM_PARAM_FILE)
    #ld.add_action(SLAM_TOOLBOX)

    #ld.add_action(CONE)

    return ld


###https://arxiv.org/pdf/2311.14276

"""
Node( #ODOMETRIA
            package='puente_ros',
            namespace='',
            executable='puente_ros_odom',
            name='puente_ros_odom',
            arguments=['--ros-args', '--log-level', log]
        ),
        Node( #LIDAR
            package='puente_ros',
            namespace='',
            executable='puente_ros_lidar',
            name='puente_ros_lidar',
            arguments=['--ros-args', '--log-level', log]
        ),
        Node( #CAMARA
            package='puente_ros',
            namespace='',
            executable='puente_ros_camara',
            name='puente_ros_camara',
            arguments=['--ros-args', '--log-level', log]
        ),
        Node( #CONVERSION POINTCLOUD A LASERSCAN
            package='pointcloud_to_laserscan', executable='pointcloud_to_laserscan_node',
            remappings=[('scan_in', 'scan_in'),
                       ('scan','scan_pre')],
            name='pointcloud_to_laserscan'
        ),
        Node( #AÑADIR TIME_STAMP A LASERSCAN
            package='puente_ros',
            namespace='',
            executable='puente_ros_laser',
            name='puente_ros_laser',
            arguments=['--ros-args', '--log-level', log]
        ),



            remappings=[('cloud_in', [LaunchConfiguration(variable_name='scanner'), '/cloud']),
                       ('scan', [LaunchConfiguration(variable_name='scanner'), '/scan'])],
            parameters=[{
                'target_frame': 'cloud',
                'transform_tolerance': 0.01,
                'min_height': 0.0,
                'max_height': 1.0,
                'angle_min': -1.5708,  # -M_PI/2
                'angle_max': 1.5708,  # M_PI/2
                'angle_increment': 0.0087,  # M_PI/360.0
                'scan_time': 0.3333,
                'range_min': 0.45,
                'range_max': 4.0,
                'use_inf': True,
                'inf_epsilon': 1.0
            }], """