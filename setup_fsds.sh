
#========================
#setup_fsds.sh
#========================

#Elaborado por Jaime Perez para el ISC 21/07/24
#Guia para la instalacion del simulador FSDS
#Instala simulador y el puente ros basado en el AirSim
#Probado en Ubuntu 22.04 y Ros2 Humble 

#El repositorio deve ir clonado en /home y de forma recursiva porque sino no descarga las dependencias
cd ~/
git clone https://github.com/FS-Driverless/Formula-Student-Driverless-Simulator.git --recurse-submodules

#Instalar AirSim
cd Formula-Student-Driverless-Simulator/AirSim
./setup.sh

#Cambiar paquete fs_msgs
#Por defecto git clona la dependencia de la rama de main pero se deve hacer de la rama de ros2
cd ../ros2/src
rm -r -f fs_msgs

git clone -b ros2 https://github.com/FS-Driverless/fs_msgs.git   #Clonar de ros2
cd ..
colcon build      #Compilar modulo ros2

cd ~/Documents/IFS06-DV
