###No se puede ejecutar archivo desde terminal

##Lanzar Simulacion
cd ~/Formula-Student-Driverless-Simulator
./FSDS.sh

##Lanzar Puente
source ~/Formula-Student-Driverless-Simulator/ros2/install/setup.sh
cd ~/Formula-Student-Driverless-Simulator/ros2
ros2 launch fsds_ros2_bridge fsds_ros2_bridge.launch.py manual_mode:=True

##Lanzar transformada de odom
source install/setup.sh
ros2 launch puente_ros puente_ros.launch.py

##Lanzar Slam
source fs_msgs/install/setup.sh  && source install/setup.sh
ros2 launch slam slam.launch.py
#Modulos aislados de Slam
ros2 run slam Cone_Detection
ros2 run slam Publicar_Mapa

##Lanzar yolo
source install/setup.sh
ros2 run yolo Yolo

##Path_planning
source fs_msgs/install/setup.sh  && source install/setup.sh
ros2 run path_planning Plan_Path
ros2 run path_planning Reset

source install/setup.sh
ros2 run control Control

##compilar solo un paquete
colcon build --packages-select coche_urdf
ros2 launch coche_urdf coche_urdf.launch.py

##full pipeline
ros2 launch full_pipeline.py

##foxglob bridge
ros2 launch foxglove_bridge foxglove_bridge_launch.xml