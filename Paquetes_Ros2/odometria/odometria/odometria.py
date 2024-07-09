"""
========================
odometria.py (v1.0)
========================

Elaborado por Lucía Herraiz y Álvaro Pérez para el ISC

IMPORTANTE: Este código funciona con datos recogidos solamente en el eje X, es decir, la velocidad lineal solo tiene componente X.

Este nodo se va a encargar de la odometría del coche.
Utilizamos la velocidad lineal y angular recogida por el GSS (Ground Speed Sensor) y el ángulo de rotación de las ruedas. 
Estimamos la velocidad y rotación de cada rueda.
Calculamos la nueva posición en el eje xy tras un intervalo de tiempo.

Posibles errores en el cálculo de la posición relativa: (tener en cuenta para cuando tengamos el coche)
    · Los diámetros de las ruedas no son iguales y difieren del diámetro de fábrica.
    · Mal alineamiento de las ruedas.
    · Resolución discreta (no continua) del encoder.
    · La tasa de muestreo del encoder es discreta.
    · Desplazamiento en suelos desnivelados.
    · Desplazamiento sobre objetos inesperados que se encuentren en el suelo.
    · Patinaje de las ruedas.
"""

import rclpy
from rclpy.node import Node
import math
from nav_msgs.msg import Odometry
from geometry_msgs.msg import TwistWithCovarianceStamped
from fs_msgs.msg import ControlCommand
from std_msgs.msg import Int64
import time

# Retocar si hiciese falta
GIRO_MAXIMO_RUEDAS = 25  # en grados º
RADIO_RUEDA = 0.20  # en metros
DISTANCIA_RUEDAS = 0.80  # en metros

# Conversiones necesarias
GIRO_MAXIMO_RUEDAS = math.radians(GIRO_MAXIMO_RUEDAS)


class PosicionNode(Node):
    def __init__(self):
        super().__init__('calcular_posicion')

        # Asumimos parámetros iniciales
        self.time_anterior = time.time()
        self.time_actual = time.time()
        self.posicion_x = 0
        self.posicion_y = 0
        self.theta = 0
        self.velocidad_lineal = 0
        self.velocidad_angular = 0
        self.angulo_giro = 0
        # v en m/s
        self.v_rueda_izq = 0
        self.v_rueda_der = 0
        # ω = velocidad angular en radianes
        self.w_rueda_der = 0
        self.w_rueda_izq = 0

        # Publicación
        self.odom_pub = self.create_publisher(Odometry, 'odom', 10)

        # Suscripciones
        self.gss_subscriber = self.create_subscription(
            TwistWithCovarianceStamped,
            '/gss',
            self.gss_callback,
            10)
        self.control_command_sub = self.create_subscription(
            ControlCommand,
            '/control_command',
            self.control_command_callback,
            10)

    def gss_callback(self, msg: TwistWithCovarianceStamped):
        """
        Recoge los datos del gss de la velocidad del coche del simulador.

        Args:
            msg (TwistWithCovarianceStamped): Mensaje con la velocidad y la covarianza.
        """
        self.velocidad_angular = msg.twist.twist.angular.z
        self.velocidad_lineal = msg.twist.twist.linear.x

    def control_command_callback(self, msg: ControlCommand):
        """
        Recoge el ángulo de las ruedas del coche.

        Args:
            msg (ControlCommand): Mensaje con el ángulo de las ruedas.
        """
        self.angulo_giro = msg.steering * GIRO_MAXIMO_RUEDAS

    def estimar_rotaciones_ruedas(self):
        """
        Estima la rotación de cada rueda, dadas una velocidad lineal y angular del coche.
        """
        self.v_rueda_izq = self.velocidad_lineal - \
            (self.velocidad_angular * DISTANCIA_RUEDAS) / 2
        self.v_rueda_der = self.velocidad_lineal + \
            (self.velocidad_angular * DISTANCIA_RUEDAS) / 2

        self.w_rueda_izq = self.v_rueda_izq / RADIO_RUEDA
        self.w_rueda_der = self.v_rueda_der / RADIO_RUEDA

    def calcular_nueva_posicion(self):
        """
        Calculamos la distancia recorrida por el coche utilizando la ω (velocidad angular).

        Se guarda la nueva posición en el eje xy.
        """
        # Velocidad media del coche
        v_media = (self.v_rueda_der + self.v_rueda_izq) / 2

        # Calculamos Δt
        self.time_actual = time.time()
        delta_t = self.time_actual - self.time_anterior
        self.time_anterior = time.time()

        # Calculamos la tasa de giro del coche
        tasa_giro = (self.velocidad_lineal / DISTANCIA_RUEDAS) * \
            math.tan(self.angulo_giro)
        
        # Cálculo de δθ
        delta_theta = tasa_giro * delta_t

        # Variación en los ejes X e Y
        delta_x = v_media * math.cos(self.theta + delta_theta / 2) * delta_t
        delta_y = v_media * math.sin(self.theta + delta_theta / 2) * delta_t

        # Se guardan las nuevas posiciones y ángulo absolutos
        self.theta += delta_theta
        self.posicion_x += delta_x
        self.posicion_y += delta_y

        # Añadido para printear posiciones en testing
        self.get_logger().info(
            f"Posición estimada: x={self.posicion_x}, y={self.posicion_y}")

    def publicar_odometria(self):
        """
        Publica los datos de odometría en el topic 'odom'.
        """
        odom = Odometry()
        odom.header.stamp = self.get_clock().now().to_msg()
        odom.header.frame_id = 'odom'
        odom.child_frame_id = 'base_link'

        # Ajustar la posición
        odom.pose.pose.position.x = self.posicion_x
        odom.pose.pose.position.y = self.posicion_y
        odom.pose.pose.position.z = 0.0

        # Convertimos yaw (theta) a cuaternión
        [qx, qy, qz, qw] = self.convertir_euler_a_cuaternion(0, 0, self.theta)
        odom.pose.pose.orientation.x = qx
        odom.pose.pose.orientation.y = qy
        odom.pose.pose.orientation.z = qz
        odom.pose.pose.orientation.w = qw

        # Ajustar la velocidad
        odom.twist.twist.linear.x = self.velocidad_lineal
        odom.twist.twist.angular.z = self.velocidad_angular

        # Publicar
        self.odom_pub.publish(odom)

    def convertir_euler_a_cuaternion(self, roll, pitch, yaw):
        """
        Convierte ángulos de Euler a una cuaternión.

        Args:
            roll (float): Ángulo de rotación alrededor del eje X.
            pitch (float): Ángulo de rotación alrededor del eje Y.
            yaw (float): Ángulo de rotación alrededor del eje Z.

        Returns:
            list: La cuaternión correspondiente [x, y, z, w].
        """
        qx = math.sin(roll / 2) * math.cos(pitch / 2) * math.cos(yaw / 2) - \
            math.cos(roll / 2) * math.sin(pitch / 2) * math.sin(yaw / 2)
        qy = math.cos(roll / 2) * math.sin(pitch / 2) * math.cos(yaw / 2) + \
            math.sin(roll / 2) * math.cos(pitch / 2) * math.sin(yaw / 2)
        qz = math.cos(roll / 2) * math.cos(pitch / 2) * math.sin(yaw / 2) - \
            math.sin(roll / 2) * math.sin(pitch / 2) * math.cos(yaw / 2)
        qw = math.cos(roll / 2) * math.cos(pitch / 2) * math.cos(yaw / 2) + \
            math.sin(roll / 2) * math.sin(pitch / 2) * math.sin(yaw / 2)
        return [qx, qy, qz, qw]


def calcular_posicion(args=None):
    rclpy.init(args=args)
    pos_node = PosicionNode()

    rclpy.spin(pos_node)
    rclpy.shutdown()
