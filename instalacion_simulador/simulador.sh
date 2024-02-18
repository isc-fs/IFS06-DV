#!/bin/bash

locale
sudo apt update && sudo apt install locales -y
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings
sudo apt install software-properties-common
sudo add-apt-repository universe
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update
sudo apt upgrade
sudo apt install ros-galactic-desktop -y
sudo apt install -y \
    ros-galactic-gazebo-ros ros-galactic-rviz2 ros-galactic-joint-state-publisher \
    ros-galactic-ackermann-msgs ros-galactic-xacro \
    ros-galactic-yaml-cpp-vendor libyaml-cpp-dev
# Replace ".bash" with your shell if you're not using bash
# Possible values are: setup.bash, setup.sh, setup.zsh
source /opt/ros/galactic/setup.bash
sudo sh -c 'echo "deb [arch=amd64,arm64] http://repo.ros2.org/ubuntu/main `lsb_release -cs` main" > /etc/apt/sources.list.d/ros2-latest.list'
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo apt update
sudo apt install python3-pip -y
sudo apt install python3-colcon-common-extensions -y
pip3 install colcon-common-extensions -U
pip3 install colcon-cmake
sudo apt install git -y
mkdir -p simulador
# mkdir -p simulador_exec
cd simulador/
git clone https://gitlab.com/eufs/eufs_msgs.git
git clone https://gitlab.com/eufs/eufs_sim.git
git clone https://gitlab.com/eufs/eufs_rviz_plugins
# echo 'export EUFS_MASTER=home/simulator/simulador/simulador_exec' >> ~/.bashrc
# source ~/.bashrc
sudo apt-get install python3-rosdep -y
sudo rosdep init
rosdep update
rosdep install --from-paths $EUFS_MASTER --ignore-src -r -y
sudo apt install ros-galactic-joint-state-publisher python3-tk -y

cd simulador_exec
colcon build
. install/setup.bash
ros2 launch eufs_launcher eufs_launcher.launch.py


