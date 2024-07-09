import numpy
from math import atan2, pi, sqrt
import time

from rclpy.qos import QoSDurabilityPolicy, QoSHistoryPolicy, QoSProfile, QoSReliabilityPolicy

QOS_LATEST = QoSProfile(
    reliability=QoSReliabilityPolicy.BEST_EFFORT,
    history=QoSHistoryPolicy.KEEP_LAST,
    depth=1,
    durability=QoSDurabilityPolicy.VOLATILE,
)

def unit_vector(vector):
    return vector / numpy.linalg.norm(vector)

millis = lambda: int(round(time.time() * 1000))

def wrap_to_pi(angle: float) -> float:  # in rads
    return (angle + pi) % (2 * pi) - pi

def angle(p1, p2) -> float:
    x_disp = p2[0] - p1[0]
    y_disp = p2[1] - p1[1]
    return atan2(y_disp, x_disp)

class Derivada():
    def __init__(self):
        self.v_ant=0
        self.t_ant=0

    def cal(self,v_nuevo):
        dev=((v_nuevo-self.v_ant)/(millis()-self.t_ant))*1000.0
        self.t_ant=millis()
        self.v_ant=v_nuevo
        return dev
