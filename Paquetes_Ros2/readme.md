# Ros2 Pipeline

Con la siguiente estructura se simplifica el proceso de arrancar todo el pipeline y no hacen falta abrir 10 terminales. Solo 4 xd

## Arancar el pipeline
#### Antes de empezar:
1. Instalar ros2 humble
2. Instalar el simulador. Instruciones en la rama de FSDS-Simulacion

#### Compilar paquetes:
La primera vez que se quiera arrancar el pipeline habra que compilarlo.
1. Colocarse en la carpeta de Paquetes_Ros2. Es decir en la que esta este archivo
2. Ejecutar `colcon build`
3. ros2 compilar todos los paquetes

#### Una vez que estan compilado:
Una vez que los paquetes estan compilados. Lanzar el pipeline:
1. En un terminal: Colocarse en la carpeta del simulador `cd ~/Formula-Student-Driverless-Simulator`
2. Arrancar el simulador `./FSDS.sh` e iniciarlo pulsando "Run simulation"
3. En un nuevo terminal: Ejecutar `source ~/Formula-Student-Driverless-Simulator/ros2/install/setup.sh`
4. Lanzar el puente ros `ros2 launch fsds_ros2_bridge fsds_ros2_bridge.launch.py`
5. En otro terminal: Colocarse en la carpeta de Paquetes_Ros2. Es decir en la que esta este archivo
6. Lanzar el pipeline Ejecutando `source install/setup.sh `
7. Y a continuacion `ros2 launch full_pipeline.py`

Este proceso debe repetirse cada vez que se quiera lanzar el pipeline.
Pero solo se debe volver a compilar si se modifica el codigo

## Como funciona la compilacion
Compilando desde Paquetes_Ros2 se crea un paquete que contiene a los otros.
De esta manera desde Paquetes_Ros2 se puede llamar al resto de dependencias y crear un launch global. Ademas se puede compilar todo sin necesidad de recorrer cada paquete de forma individual.

Los paquetes se comportar como un todo o de forma individual dependiendo de como se aceda a ellos.
Es decir, que si se modifica un paquete y se quiere lanzar desde un archivo launch global (por ejemplo: full pipeline.py) se deve volver a compilar todos los paquetes desde la carpeta de Paquetes_Ros2. Pero si se lanza el nodo de forma individual no es necesario parar y recompilar todo el piepline. Se puede compilar solo desde la carpeta de ese paquete y lanzar el nodo de forma manual.

Esto es until durante le proceso de resarrolo. Por ejemplo: Si estoy desarrollando control configuro un launch gloval que aranque los modulos con los que interactua mi nodo. Y leugo cada vez que modifico mi nodo recompilo solo ese paquete y lo lanzo manualmente.

Con este workflow se ahora mucho tiempo.

## Otras cosas importantes
1. Ya no es necesario añadir fs_msgs a cada paquete
2. Solo hay que hacer `source` una vez
3. Los comandos de `launch_pipeline.sh` siguen funcionando igual.
4. Se puede reiniciar el simulador sin apagar y volver a encender con `ros2 run path_planning Reset`
