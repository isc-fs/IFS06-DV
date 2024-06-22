from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'puente_ros'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='JaimePerez',
    maintainer_email='JaimePerez@todo.todo',
    description='PuenteFSDSaROS',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'puente_ros_laser = puente_ros.puente_ros:laser_stamp',
            'puente_ros_TF = puente_ros.puente_ros:TF',
        ],
    },
)
