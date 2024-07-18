import os
from os.path import isfile, join

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import xacro

def get_argument(context, arg):
    return LaunchConfiguration(arg).perform(context)


def process_xacro(context, *args, **kwargs):
    urdf_model = get_argument(context, "urdf_model")
    base_frame = get_argument(context, "base_frame")
    display_car = get_argument(context, "display_car")

    xacro_path = join(
        get_package_share_directory("coche_urdf"),
        "urdf",
        urdf_model,
    )
    print(xacro_path)
    urdf_path = join(
        get_package_share_directory("coche_urdf"),
        "urdf",
        "processed.urdf",
    )
    print(urdf_path)

    # remove old file and create new one
    if isfile(urdf_path):
        os.remove(urdf_path)
        os.mknod(urdf_path)

    doc = xacro.process_file(
        xacro_path,
        mappings={
            "base_frame": base_frame,
            "display_car": display_car,
        },
    )
    robot_description = doc.toprettyxml(indent="  ")

    out = xacro.open_output(urdf_path)
    out.write(doc.toprettyxml(indent="  "))

    return [
        Node(
            package="coche_urdf",
            executable="Publicar_comado",
            output="screen",
        ),
        Node(
            package="joint_state_publisher",
            executable="joint_state_publisher",
            output="screen",
            parameters=[
                {
                    "rate": 200,
                    "source_list": ["joint_states_t"],
                }
            ],
            arguments=[urdf_path,"--ros-args", "--log-level", "info"],
        ),
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            output="screen",
            parameters=[
                {
                    "robot_description": robot_description,
                    "rate": 200,
                }
            ],
            arguments=["--ros-args", "--log-level", "info"],
        ),
    ]

def generate_launch_description():
    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "base_frame",
                default_value="fsds/FSCar",
                description="Base frame of the vehicle",
            ),
            DeclareLaunchArgument(
                "urdf_model",
                default_value="ifs06.urdf.xacro",
                description="URDF Model to use (from vehicle_urdf/urdf)",
            ),
            DeclareLaunchArgument(
                "display_car",
                default_value="true",
                description="Display the car in rviz",
            ),
            OpaqueFunction(function=process_xacro),
        ]
    )