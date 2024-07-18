"""
========================
odometria.py (v1.0)
========================

Elaborado por Álvaro Pérez y Lucía Herraiz para el ISC

IMPORTANTE: Este código funciona con datos recogidos solamente en el eje X, es decir, la velocidad lineal solo tiene componente X.

Este nodo se va a encargar de la odometría del coche.
Utilizamos la velocidad lineal y angular recogida por el gss (ground speed sensor) y el ángulo de rotación de las ruedas. 
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

Asunciones:
    · El punto de referencia cogido está en el centro del coche, ya que el simulador coge todas las referencias desde ese punto.
"""

import rclpy
from rclpy.node import Node
import math
from nav_msgs.msg import Odometry
from geometry_msgs.msg import TwistWithCovarianceStamped
from fs_msgs.msg import ControlCommand
import time

# Retocar si hiciese falta
GIRO_MAXIMO_RUEDAS = 25  # en grados º
RADIO_RUEDA = 0.20  # en metros
DISTANCIA_RUEDAS_PARALELAS = 0.80  # en metros
DISTANCIA_RUEDAS_LONGITUDINAL = 1.20 # en metros
DISTANCIA_RUEDAS_TRASERAS_CENTRO_COCHE = 0.78 # en metros


class PosicionNode(Node):
    def __init__(self):
        super().__init__('calcular_posicion')

        # Asumimos parámetros iniciales
        self.time_anterior = time.time()
        self.time_actual = time.time()
        self.posicion_x = 0 # en metros
        self.posicion_y = 0 # en metros
        self.theta = 0 # en radianes
        self.delta = 0 # en radianes

        # Parámetros para testing (simulador)
        self.posicion_real_x = 0
        self.posicion_real_y = 0
        self.velocidad_real_x = 0
        self.velocidad_real_y = 0

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
        self.odom_sub = self.create_subscription(Odometry, 
            'testing_only/odom',
            self.odom_callback,
            10)

    def gss_callback(self, msg: TwistWithCovarianceStamped):
        """
        Recoge los datos del gss de la velocidad del coche del simulador.
        Se mandan los datos actualizados al coche con la tasa de refresco del gss.

        Args:
            msg (TwistWithCovarianceStamped): Mensaje con la velocidad y la covarianza.
        """
        self.v = msg.twist.twist.linear.x

        self.calcular_estados()
        self.launch_debugger()
        self.calcular_posicion()

    def control_command_callback(self, msg: ControlCommand):
        """
        Recoge el ángulo de las ruedas del coche.

        Args:
            msg (ControlCommand): Mensaje con el ángulo de las ruedas.
        """
        self.delta = math.radians(msg.steering * GIRO_MAXIMO_RUEDAS)

    def odom_callback(self, msg: Odometry):
        """
        Recoge la posición y velocidad reales del simulador.

        Args:
            msg (ControlCommand): Mensaje con el ángulo de las ruedas.
        """
        self.posicion_real_x = msg.pose.pose.position.x
        self.posicion_real_y = msg.pose.pose.position.y
        self.velocidad_real_x = msg.twist.twist.linear.x
        self.velocidad_real_y = msg.twist.twist.linear.y

    def calcular_modelo(self) -> list:
        """
        Calcula los diferenciales de x, y, theta.

        Returns:
            list: Devuelve una lista con los datos necesarios para calcular los estados.
        """
        # Calcular el ángulo de movimiento del coche (beta)
        beta = math.atan(DISTANCIA_RUEDAS_TRASERAS_CENTRO_COCHE * math.tan(self.delta) / DISTANCIA_RUEDAS_LONGITUDINAL)

        # Calcular los cambios de posición y ángulo del coche respecto de la posición inicial
        dx = self.v * math.cos(beta + self.theta)
        dy = self.v * math.sin(beta + self.theta)
        dtheta = (self.v / DISTANCIA_RUEDAS_TRASERAS_CENTRO_COCHE) * math.sin(beta) 

        return [dx, dy, dtheta]

    def calcular_estados(self):
        """
        Actualiza las variables de estado utilizando los cálculos del modelo.
        """
        [dx, dy, dtheta] = self.calcular_modelo()
        
        # Calcular el delta de tiempo
        self.time_actual = time.time()
        delta_t = self.time_actual - self.time_anterior
        self.time_anterior = self.time_actual

        # Actualizar las variables de estado
        self.posicion_x += (dx * delta_t)
        self.posicion_y += (dy * delta_t)
        self.theta += (dtheta * delta_t)

        # Guardar velocidades para debuggear
        self.v_x = dx
        self.v_y = dy

    def launch_debugger(self):
        """
        Ejecuta un print en terminal para comparar velocidades reales y estimadas.
        """
        self.get_logger().info(f"Velocidad: x={self.velocidad_real_x - self.v_x}, y={self.velocidad_real_y - self.v_y}")
        # self.get_logger().info(f"Ángulo: {self.theta}")

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

        # Convertir yaw (theta) a cuaternión
        [qx, qy, qz, qw] = convertir_euler_a_cuaternion(0, 0, self.theta)
        odom.pose.pose.orientation.x = qx
        odom.pose.pose.orientation.y = qy
        odom.pose.pose.orientation.z = qz
        odom.pose.pose.orientation.w = qw

        # Ajustar la velocidad
        odom.twist.twist.linear.x = self.v

        # Publicar
        self.odom_pub.publish(odom)

def convertir_euler_a_cuaternion(roll, pitch, yaw):
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
    print("Hola")
    rclpy.init(args=args)
    pos_node = PosicionNode()
    print("Hola")

    rclpy.spin(pos_node)
    rclpy.shutdown()
