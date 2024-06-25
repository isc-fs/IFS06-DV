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

from sklearn.cluster import DBSCAN

def distancia(x_c,y_c,x,y):         ###Distancia entre dos deteciones
    return numpy.sqrt((x_c-x)**2 + (y_c-y)**2)

class Cono():
    """
    Aqui se puenen agregar todas las caracteristicas del cono que se desean rastrear
    """
    def __init__(self):
        self.x=0
        self.y=0

class Mapa():    ###Mapa de features
    def __init__(self):
        self.conos=[]
        self.deteciones=[]

    def add_detecion(self,x,y,t):
        """Añade una detecion al mapa
            Se consideran dos deteciones iguales si estan a menos de 1 cm.
            El tamaño de la lista determina la longitud del mapa local. 

        Args:
            x (float): Cordenada en x de la detecion a añadir
            y (float): Cordenada en y de la detecion a añadir
            t (float): Transformada de la cordenada del coche a la odometria
        """

        ###Tranformar de un sistema de referencia del coche a odom
        point_source = Point(x=x, y=y, z=0.0)
        point_source=do_transform_point(geometry_msgs.msg.PointStamped(point=point_source),t)

        candidato_detecion=[]
        candidato_detecion.append(point_source.point.x)
        candidato_detecion.append(point_source.point.y)

        encontrado=False
        for detecion in self.deteciones:
            if(distancia(detecion[0],detecion[1],candidato_detecion[0],candidato_detecion[1])<0.01):
                encontrado=True
                break

        if not encontrado:
            self.deteciones.append(candidato_detecion)

        ###Longitud de la lista de detecione determina el tamaño del mapa
        ###200 para competi 500-1000 para test con odom perfecta
        ###1500 o mas para skid pad
        long_list_deteciones=200
        if len(self.deteciones)>long_list_deteciones:  
            for i in range(10):     ###Eliminar de 10 cada vez para minimizar "parpadeo" de las prediciones
                self.deteciones.pop(0)

    def actualizar_mapa(self):
        """Actualiza el mapa.
            Primero realiza clusterign con las deteciones
            Segundo calcula la media de cada cluster
        """
        ###Modelo de Clustering para conos
        clust_model = DBSCAN(eps=0.5, min_samples=1)  ###min_sample=1 porque hay muy pocos falsos positivos
        labels = clust_model.fit_predict(self.deteciones)

        deteciones_separadas=[[] for i in range(max(labels)+1)]
        for (i,label) in enumerate(labels):
            if label==-1:
                continue
            deteciones_separadas[label].append(self.deteciones[i])

        ###Calcular media de las deteciones en cada cluster
        self.conos=[]
        for deteciones_cono in deteciones_separadas:
            x_avr=0.0
            y_avr=0.0
            for detecion in deteciones_cono:
                x_avr=x_avr+detecion[0]
                y_avr=y_avr+detecion[1]
            c=Cono()
            c.x=x_avr/len(deteciones_cono)
            c.y=y_avr/len(deteciones_cono)
            self.conos.append(c)