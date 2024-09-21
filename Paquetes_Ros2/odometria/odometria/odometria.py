import rclpy
from rclpy.node import Node
import math
from nav_msgs.msg import Odometry
from geometry_msgs.msg import TwistWithCovarianceStamped
from fs_msgs.msg import ControlCommand
import time

# Constantes
GIRO_MAXIMO_RUEDAS = 25  # en grados º 25
RADIO_RUEDA = 0.20  # en metros 0.20
DISTANCIA_RUEDAS_PARALELAS = 1.00  # en metros 0.80
DISTANCIA_RUEDAS_LONGITUDINAL = 1.20  # en metros 1.20
DISTANCIA_RUEDAS_TRASERAS_CENTRO_COCHE = 0.77  # en metros 0.78


class PosicionNode(Node):
    def __init__(self):
        super().__init__('calcular_posicion')

        # Parámetros Iniciales
        self.time_anterior = time.time()
        self.time_actual = time.time()
        self.posicion_x = 0  # en metros
        self.posicion_y = 0  # en metros
        self.theta = 0  # en radianes
        self.delta = 0  # en radianes

        # Inicializar variables para recoger datos del simulador
        self.posicion_real_x = 0
        self.posicion_real_y = 0
        self.velocidad_real_x = 0
        self.velocidad_real_y = 0

        # Flag Modo Debug
        self.debug_mode = True  # True si se quiere debugear

        # Publisher
        self.odom_pub = self.create_publisher(Odometry, 'odom', 10)

        # Subscriptions
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
        self.v_x = msg.twist.twist.linear.x

        self.time_actual = time.time()

        self.calcular_estados()
        if self.debug_mode:
            self.debug()

    def control_command_callback(self, msg: ControlCommand):
        """
        Recoge el ángulo de las ruedas del coche.

        Args:
            msg (ControlCommand): Mensaje con el ángulo de las ruedas.
        """

        if msg.steering > 1:
            msg.steering = 1.0

        if msg.steering < -1:
            msg.steering = -1.0

        self.delta = math.radians(msg.steering * GIRO_MAXIMO_RUEDAS)

        if self.debug_mode:
            self.debug()

    def odom_callback(self, msg: Odometry):
        """
        Recoge la posición y velocidad reales del simulador.

        Args:
            msg (Odometry): Mensaje con la posición y velocidad.
        """
        self.posicion_real_x = msg.pose.pose.position.x
        self.posicion_real_y = msg.pose.pose.position.y
        self.velocidad_real_x = msg.twist.twist.linear.x
        self.velocidad_real_y = msg.twist.twist.linear.y

        if self.debug_mode:
            self.debug()

    def calcular_estados(self):
        """
        Calcula los estados del coche basados en la velocidad y el ángulo de las ruedas.
        """
        delta_time = self.time_actual - self.time_anterior
        self.time_anterior = self.time_actual

        # Actualizar posición y orientación
        self.posicion_x += self.v_x * delta_time * math.cos(self.theta)
        self.posicion_y += self.v_x * delta_time * math.sin(self.theta)
        self.theta += self.delta * delta_time

        # Convertir Euler angles to quaternion
        [qx, qy, qz, qw] = convertir_euler_a_cuaternion(0, 0, self.theta)
        odom = Odometry()
        odom.header.stamp = self.get_clock().now().to_msg()
        odom.header.frame_id = 'odom'
        odom.pose.pose.position.x = self.posicion_x
        odom.pose.pose.position.y = self.posicion_y
        odom.pose.pose.orientation.x = qx
        odom.pose.pose.orientation.y = qy
        odom.pose.pose.orientation.z = qz
        odom.pose.pose.orientation.w = qw

        # Ajustar la velocidad
        odom.twist.twist.linear.x = self.v_x

        # Publicar
        self.odom_pub.publish(odom)

        if self.debug_mode:
            self.debug()

    def debug(self):
        """
        Función de debug para registrar valores y verificar posibles errores.
        """
        self.get_logger().info(f"Tiempo actual: {self.time_actual}")
        self.get_logger().info(f"Tiempo anterior: {self.time_anterior}")
        self.get_logger().info(
            f"Delta time: {self.time_actual - self.time_anterior}")
        self.get_logger().info(
            f"Posición: ({self.posicion_x}, {self.posicion_y})")
        self.get_logger().info(f"Orientación (theta): {self.theta}")
        self.get_logger().info(f"Ángulo de dirección (delta): {self.delta}")
        self.get_logger().info(f"Velocidad lineal (v_x): {self.v_x}")
        self.get_logger().info(
            f"Posición real: ({self.posicion_real_x}, {self.posicion_real_y})")
        self.get_logger().info(
            f"Velocidad real: ({self.velocidad_real_x}, {self.velocidad_real_y})")

        # Verificar posibles errores
        if self.time_actual < self.time_anterior:
            self.get_logger().error("Error: time_actual es menor que time_anterior")
        if not (-math.pi <= self.theta <= math.pi):
            self.get_logger().error("Error: theta está fuera de los límites")
        if not (-math.pi <= self.delta <= math.pi):
            self.get_logger().error("Error: delta está fuera de los límites")


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
    rclpy.init(args=args)
    pos_node = PosicionNode()

    rclpy.spin(pos_node)
    rclpy.shutdown()
