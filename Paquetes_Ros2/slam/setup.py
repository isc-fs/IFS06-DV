from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'slam'

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
    maintainer='jaime',
    maintainer_email='jaimeperezgil21@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'Cone_Detection = slam.cone_detection_node:cone_detection',
            'Cone_Laser = slam.slam:cone_laser',
            'Publicar_Mapa = slam.slam:publicar_mapa',
            'Publicar_Track = slam.slam:publicar_track'
        ],
    },
)

