"""
========================
map.py (v1.0)
========================

Elaborado por Jaime Perez para el ISC
Mapa de Features Basico
Contine:

Clase Cono: Con los parametros de cada cono. Posicon, n_veces_viso. (Futuro: Color, Tipo, Forma_de_deteccion)

Clase Mapa: Contiene lista de los Conos en el mapa y add_cono que añade un cono al mapa si no esta ya.
"""

import sys
import os
import time
import numpy
import math

import rclpy
from rclpy.node import Node

from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from tf2_geometry_msgs import do_transform_point
from geometry_msgs.msg import Point
import geometry_msgs

def distancia(cono,x,y):
    return numpy.sqrt((cono.x-x)**2 + (cono.y-y)**2)

class Cono():
    """
    Aqui se puenen agregar todas las caracteristicas del cono que se desean rastrear
    """
    def __init__(self):
        self.x=0
        self.y=0

        self.n_visto=0

class Mapa():    ###Mapa de features
    def __init__(self):
        self.conos=[]

    def add_cono(self,x,y,t):
        """Añade un cono a el mapa
            Para hacer esto se compueba si el cono que se quiere añadir esta a mas de un metro de otro del mapa
            si es asi se añade. Si no se apunta que se ha vuelto a ver el otro cono

        Args:
            x (float): Cordenada en x del cono a añadir
            y (float): Cordenada en y del cono a añadir
            t (float): Transformada de la cordenada del coche a la odometria
        """
        i=0
        f=False

        cono_nuevo=Cono()               ###Tranformar de un sistema de referencia del coche a odom
        point_source = Point(x=x, y=y, z=0.0)
        point_source=do_transform_point(geometry_msgs.msg.PointStamped(point=point_source),t)
        cono_nuevo.x=point_source.point.x
        cono_nuevo.y=point_source.point.y
        
        for cono in self.conos:  
            if(distancia(cono,cono_nuevo.x,cono_nuevo.y)<0.1):
                cono.n_visto+=1
                f=True
                break

            self.conos[i]=cono
            i+=1

        if f==False:
            cono_nuevo.n_visto+=1
            if len(self.conos)>100:              ###Maximo numero de conos permitidos para evitar que se crashe si se le va la pinza
                self.conos.pop(0)
            self.conos.append(cono_nuevo)
            