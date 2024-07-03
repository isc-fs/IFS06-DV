"""
========================
odometria.py (v1.0)
========================

Elaborado por Lucía Herraiz y Álvaro Pérez para el ISC

Este nodo se va a encargar de la odometria del coche. A partir del giro de las ruedas y la velocidad lineal estima la posición relativa
 (luego desarrollamos esto jajaj)

 Posibles errores en el cálculo de la posición relativa: (tener en cuenta para cuando tengamos el coche)
    Los diámetros de las ruedas no son iguales y difieren del diámetro de fábrica.
    Mal alineamiento de las ruedas.
    Resolución discreta (no continua) del encoder.
    La tasa de muestreo del encoder es discreta.
    Desplazamiento en suelos desnivelados.
    Desplazamiento sobre objetos inesperados que se encuentren en el suelo.
    Patinaje de las ruedas debido a: 
"""

import rclpy
from rclpy.node import Node
import math
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseWithCovarianceStamped
from geometry_msgs.msg import Twist
from std_msgs.msg import Int64
import time


def rotaciones_rueda_a_distancia():
    pass


class PosicionNode(Node):
    def __init__(self):
        super().__init__('calcular_posicion_node')

        self.posicion_x = 0
        self.posicion_y = 0 #Asumimos que parte de estos parámetros
        self.w_rueda_der = 0 #w = Velocidad angular
        self.w_rueda_izq = 0
        self.prev_update_time = time.time()

        self.radio_rueda = 10 #Hay que buscar estos datos en el modelo del coche
        self.distancia_ruedas = 10

        self.odom_pub = self.create_publisher(Odometry,"odom",10)
        self.cmd_vel_sub = self.create_subscription(Twist,"cmd_vel",'CALLBACK',10)

        self.rueda_der_subscriber = self.create_subscription(PoseWithCovarianceStamped,'/gss','CALLBACK',10)
        self.rueda_izq_subscriber = self.create_subscription()

    def calcular_nueva_posicion(self):
        """Utilizamos: vec_pos = vec_pos_0 + 'matriz'*tiempo
        Este proceso se hará iterativamente con incrementos de tiempo tan pequeños que W se considera constante.
        """        
        pass
        
def calcular_posicion(args=None):
    rclpy.init(args=args)
    pos_node = PosicionNode()

    rclpy.spin(pos_node)
    rclpy.shutdown()