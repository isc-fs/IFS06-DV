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
        super().__init__('calcular_posicion')

        # Asumimos parámetros iniciales
        self.time_anterior = time.time()
        self.time_actual = time.time()
        self.posicion_x = 0
        self.posicion_y = 0
        self.theta = 0
        self.velocidad_lineal = 0
        self.velocidad_angular = 0
        self.posicion_real_x = 0
        self.posicion_real_y = 0
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
            self.cmd_vel_callback,
            10)
        self.pos_subscriber = self.create_subscription(
            PoseWithCovarianceStamped,
            '/gss',
            self.pos_callback,
            10)

    def cmd_vel_callback(self, msg: Twist):
        """
        Controla el mensaje de cmd_vel.

        Args:
            msg (Twist): Mensaje con las velocidades lineal y angular.
        """
        self.velocidad_lineal = msg.linear.x
        self.velocidad_angular = msg.angular.z

        self.estimar_rotaciones_ruedas()
        self.calcular_nueva_posicion()
        self.publicar_odometria()

    # No utilizo esta función ya que son datos directos del simulador. Se usará para comparar.
    def pos_callback(self, msg: PoseWithCovarianceStamped):
        """
        Recoge los datos del gss de la posición del coche del simulador.

        Args:
            msg (PoseWithCovarianceStamped): Mensaje con la posición y la covarianza.
        """
        pos = msg.pose.pose

        self.posicion_real_x = pos.position.x
        self.posicion_real_y = pos.position.y

    def estimar_rotaciones_ruedas(self):
        """
        Estima la rotación de cada rueda, dadas una velocidad lineal y angular del coche.
        """
        self.v_rueda_izq = self.velocidad_lineal - \
            (self.velocidad_angular * self.distancia_ruedas) / 2
        self.v_rueda_der = self.velocidad_lineal + \
            (self.velocidad_angular * self.distancia_ruedas) / 2

        self.w_rueda_izq = self.v_rueda_izq / self.radio_rueda
        self.w_rueda_der = self.v_rueda_der / self.radio_rueda

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

        delta_x = v_media * math.cos(self.theta + delta_theta / 2) * delta_t
        delta_y = v_media * math.sin(self.theta + delta_theta / 2) * delta_t

        self.theta += delta_theta
        self.posicion_x += delta_x
        self.posicion_y += delta_y

        # Añadido para printear posiciones en testing

        self.get_logger().info(f"Posición estimada: x={self.posicion_x}, y={self.posicion_y}")
        self.get_logger().info(f"Posición real: x={self.posicion_real_x}, y={self.posicion_real_y}")


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

        quat = self.convertir_euler_a_cuaternion(0, 0, self.theta)
        odom.pose.pose.orientation.x = quat[0]
        odom.pose.pose.orientation.y = quat[1]
        odom.pose.pose.orientation.z = quat[2]
        odom.pose.pose.orientation.w = quat[3]

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
