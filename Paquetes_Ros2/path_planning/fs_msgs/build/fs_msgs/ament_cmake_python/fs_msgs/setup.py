from setuptools import find_packages
from setuptools import setup

setup(
    name='fs_msgs',
    version='0.1.1',
    packages=find_packages(
        include=('fs_msgs', 'fs_msgs.*')),
)
