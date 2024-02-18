Pasos para la instalación del simulador EUFS SIM
1. Crear una máquina virtual (se recomienda virtualbox) de Ubuntu 20.04 
2. Una vez creada la máquina y realizado el proceso de instalación, pasar los dos archivos .sh a la máquina
3. El archivo simulador.sh debe estar en la ruta \~ (home/usuario). Si se desconoce, abrir una terminal e introducir \
cd \
pwd
4. Ejecutar los siguientes comandos desde \~:\
export EUFS_MASTER="\~/simulador"\
sudo -E bash simulador.sh
5. Esperar hasta que se complete la instalación e introducir y si es necesario
6. El simulador se puede ejecutar desde cualquier ubicación en la que esté presente ejecutar_sim.sh con el siguiente comando:\
sudo -E bash ejecutar_sim.sh

IMPORTANTE: no olvidar poner el -E en los comandos de sudo, si no no funciona el simulador
