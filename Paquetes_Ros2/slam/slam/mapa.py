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

def distancia(cono,x,y):
    return numpy.sqrt((cono.x-x)**2 + (cono.y-y)**2)

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
        self.detecciones=[]

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

        ###Tranformar de un sistema de referencia del coche a odom
        point_source = Point(x=x, y=y, z=0.0)
        point_source=do_transform_point(geometry_msgs.msg.PointStamped(point=point_source),t)
        cono=[]
        cono.append(point_source.point.x)
        cono.append(point_source.point.y)
        self.detecciones.append(cono)

        if len(self.detecciones)>1500:
            self.detecciones.pop(0)
        
        """for cono in self.conos:  
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
            self.conos.append(cono_nuevo)"""

    def actualizar_mapa(self):
        clust_model = DBSCAN(eps=0.3, min_samples=5)
        labels = clust_model.fit_predict(self.detecciones)
        """separated_data = [
            numpy.array(self.detecciones[labels == label]) for label in numpy.unique(labels)
        ]"""

        deteciones_separadas=[]
        #print(max(labels))
        for i in range(150):
            deteciones_separadas.append([])
        i=0
        for label in labels:
            deteciones_separadas[label].append(self.detecciones[i])
            i=i+1


        self.conos=[]
        for deteciones_cono in deteciones_separadas:
            if len(deteciones_cono)==0:
                continue
            x_avr=0
            y_avr=0
            for detecion in deteciones_cono:
                x_avr=x_avr+detecion[0]
                y_avr=y_avr+detecion[1]
            c=Cono()
            c.x=x_avr/len(deteciones_cono)
            c.y=y_avr/len(deteciones_cono)
            self.conos.append(c)