# Puente entre FSDS a ros2 Humble

Paquete de ROS2 Humble para publicar los datos del simulador FSDS como topics.
Usando la API de python

FSDS: https://github.com/FS-Driverless/Formula-Student-Driverless-Simulator.git

## Instalacion del simulador

1. Clonar repositorio de FSDS en /home
2. Añadir a la carpeta descargada la ultima version del simulador compilado
https://github.com/FS-Driverless/Formula-Student-Driverless-Simulator/releases
3. Comprobar que funciona el simulador con `./FSDS.sh`
4. `cd Formula-Student-Driverless-Simulator/python`
5. `pip install -r requirements.txt`

## Instalacion del puente ros
1. `sudo apt-get install ros-humble-pointcloud-to-laserscan`
2. Entrar en la carpeta del paquete de ros (cd puente_ros) Puede estar donde sea...
3. Compilar con `colon build`
4. `source install/setup.sh`     No olvidar. Cada vez que se abre un terminal
5. `ros2 launch puente_ros puente_ros.launch.py`

## Topics
| Topic |  Tipo  | Descripcion |
|:-----|:--------:|------:|
| /cloud_in   | sensor_msgs/PointCloud2.msg | Datos del lidar en Nube de puntos(3D) |
| /scan   | sensor_msgs/LaserScan.msg | Datos del lidar en modo LaserScan(2D) |
| /camara   |  Imagesensor_msgs/Image.msg  |   Imagen de la camara |
| /odom   | nav_msgs/msg/Odometry.msg |    No es odometria real. Es la posicion del coche. No tiene drift |
| tf   | N/A |    Transformacion entre el sistema de referencia del coche `base_frame` y de la odometria `odom_frame`. Esta hecho asi para maximizar compativilidad con SLAM_ToolBox |


## Limitaciones

La API de Python tiene limitaciones en la velocidad a la que se puede descargar informacion del simulador. Parece que estas limitaciones van ligadas a cada sensor. Es decir que se pueden tener 10 lidar pero solo extraer de cada uno unos 80.000 ptos/seg.

En la carpeta del paquete hay un setings.json que cumple mas o menos con estas restriciones.

En las primeras lineas de `puente_ros.py` se puede activar el modo debug que imprime en pantalla la frecuencia a la que se pueden publicar los topics.

## Estructura

El paquete tiene cuatro nodos que se ejecutan de forma simultanea.
`puente_ros.launch.py` los lanza de forma simultane pero se pueden ejecutar de forma individual con:
```bash
ros2 run puente_ros puente_ros_odom
ros2 run puente_ros puente_ros_lidar
ros2 run puente_ros puente_ros_camara
ros2 run puente_ros puente_ros_laser
```