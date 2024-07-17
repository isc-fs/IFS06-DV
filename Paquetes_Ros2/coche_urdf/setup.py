from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'coche_urdf'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name+'/meshes', glob('meshes/*.dae')),
        ('share/' + package_name+'/urdf', glob('urdf/*.xacro')),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jaime',
    maintainer_email='jaimeperezgil21@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'Publicar_comado = coche_urdf.coche_urdf:publicar_joint_state',
        ],
    },
)
