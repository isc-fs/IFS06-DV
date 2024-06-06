from setuptools import find_packages, setup

package_name = 'puente_ros'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jaime',
    maintainer_email='jaime@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'puente_ros_lidar = puente_ros.puente_ros:lidar',
            'puente_ros_laser = puente_ros.puente_ros:laser_stamp',
            'puente_ros_odom = puente_ros.puente_ros:odom',
            'puente_ros_camara = puente_ros.puente_ros:camara',
            'cone = puente_ros.puente_ros:cone_detection'
        ],
    },
)
