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



class PosicionNode(Node):
    def __init__(self):
        super().__init__('calcular_posicion_node')

def calcular_posicion(args=None):
    rclpy.init(args=args)


    #rclpy.spin()
    rclpy.shutdown()