import os

from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import LifecycleNode
from launch.substitutions import (AndSubstitution, LaunchConfiguration,NotSubstitution)
from launch.actions import (DeclareLaunchArgument, EmitEvent, LogInfo,RegisterEventHandler)
from launch_ros.actions import Node
from launch import actions
import launch
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource

from ament_index_python.packages import get_package_share_directory

##Esto no funciona
## Y no esta termiado

def generate_launch_description():
    ld=LaunchDescription()

    path = os.path.dirname(os.path.realpath(__file__))
    print(path)
    print(path+'/puente_ros/puente_ros.py')

    included_launch = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([
                    path+'/puente_ros', '/launch', '/puente_ros.launch.py'])
            )
    ld.add_action(included_launch)
    return ld