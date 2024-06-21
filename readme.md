# Instalacion Simulador FSDS
1. Ejecutar `source setup_fsds.sh` . Mas informacion sobre la instalacion es ese archivo.
2. Añadir a Formula-Student-Driverless-Simulator la ultima version del simulador compilado
https://github.com/FS-Driverless/Formula-Student-Driverless-Simulator/releases
3. Comprobar que funciona el simulador con `./FSDS.sh`
4. Sustituir settings.json para configurar el simulador segun el resto del pipeline espera


Tras ejecutar `source ~/Formula-Student-Driverless-Simulator/ros2/install/setup.sh` <br />
Se puede lanzar el puente con `ros2 launch fsds_ros2_bridge fsds_ros2_bridge.launch.py manual_mode:=True`

`manual_mode:=True`=>Permite control con teclado en la ventana del simulador<br />
`manual_mode:=False`=>No permite control con teclado en la ventana del simulador. Control solo por topic de ros.