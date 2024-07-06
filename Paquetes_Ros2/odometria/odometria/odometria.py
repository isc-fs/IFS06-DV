"""
========================
odometria.py (v1.0)
========================

Elaborado por Lucía Herraiz y Álvaro Pérez para el ISC

Este nodo se va a encargar de la odometría del coche.
Utilizamos la velocidad lineal y angular recogida por el GSS (Ground Speed Sensor), estimamos la velocidad y rotación de cada rueda.
Calculamos la nueva posición en el eje xy tras un intervalo de tiempo.

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


class PosicionNode(Node):
    def __init__(self):
        super().__init__('calcular_posicion_node')

        # Asumimos parámetros iniciales
        self.time_anterior = time.time()
        self.time_actual = time.time()
        self.posicion_x = 0
        self.posicion_y = 0
        self.theta = 0
        # v en m/s
        self.v_rueda_izq = 0
        self.v_rueda_der = 0
        # ω = velocidad angular en radianes
        self.w_rueda_der = 0
        self.w_rueda_izq = 0

        # Hace falta ajustar los datos con el modelo del coche
        self.radio_rueda = 10
        self.distancia_ruedas = 10

        # Publicación
        self.odom_pub = self.create_publisher(Odometry, 'odom', 10)

        # Subscripciones
        self.cmd_vel_sub = self.create_subscription(
            Twist,
            'cmd_vel',
            'CALLBACK',
            10)
        self.pos_subscriber = self.create_subscription(
            PoseWithCovarianceStamped,
            '/gss',
            'CALLBACK',
            10)

    def cmd_vel_callback(self, msg: Twist):
        """
        Controla el mensaje de cmd_vel.

        Args:

            msg (Twist): Mensaje con las velocidades lineal y angular.
        """
        self.velocidad_lineal = msg.linear.x
        self.velocidad_angular = msg.angular.z

    # No utilizo esta función ya que son datos directos del simulador. Se usará para comparar.
    def pos_callback(self, msg: PoseWithCovarianceStamped):
        """
        Recoge los datos del gss de la posición del coche del simulador.

        Args:
            msg (PoseWithCovarianceStamped): Mensaje con la posición y la covarianza.
        """
        pos = msg.pose.pose

        x = pos.position.x
        y = pos.position.y

    def estimar_rotaciones_ruedas(self, velocidad_lineal: float, velocidad_angular: float):
        """Estima la rotación de cada rueda, dadas una velocidad lineal y angular del coche.

        Args:
            velocidad_lineal (float): La velocidad lineal del coche recogida del gss.
            velocidad_angular (float): La velocidad angular del coche recogida del gss.
        """
        self.v_rueda_izq = velocidad_lineal - \
            (velocidad_angular * self.distancia_ruedas) / 2
        self.v_rueda_der = velocidad_lineal + \
            (velocidad_angular * self.distancia_ruedas) / 2

        self.w_rueda_izq = self.v_rueda_izq/self.radio_rueda
        self.w_rueda_der = self.v_rueda_der/self.radio_rueda

    def calcular_nueva_posicion(self):
        """
        Calculamos la distancia recorrida por el coche utilizando la ω (velocidad angular).

        Se guarda la nueva posición en el eje xy.
        """
        v_media = (self.v_rueda_der + self.v_rueda_izq) / 2
        w_media = (self.w_rueda_der + self.w_rueda_izq) / 2

        self.time_actual = time.time()
        delta_t = self.time_actual - self.time_anterior
        self.time_anterior = time.time()

        delta_theta = w_media * delta_t

        delta_x = v_media * math.cos(self.theta + delta_theta/2) * delta_t
        delta_y = v_media * math.sin(self.theta + delta_theta/2) * delta_t

        self.posicion_x += delta_x
        self.posicion_y += delta_y


def calcular_posicion(args=None):
    rclpy.init(args=args)
    pos_node = PosicionNode()

    rclpy.spin(pos_node)
    rclpy.shutdown()
