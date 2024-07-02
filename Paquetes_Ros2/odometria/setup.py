from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'odometria'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    ata_files=[
        ('share/ament_index/resource_index/packages',['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lucia',
    maintainer_email='lucia.herraizcano@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'Publicar_TF = odometria.odometria:publicar_tf'
            'Calcular_Odometria = odometria.odometria:calcular_odometria' 
        ],
    },
)
