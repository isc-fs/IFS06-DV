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
        self.x=0.0
        self.y=0.0

        self.color=''

class Detecion():
    """
    Aqui se puenen agregar todas las caracteristicas del cono que se desean rastrear
    """
    def __init__(self):
        self.x=0.0
        self.y=0.0

        self.x_rel=0.0
        self.y_rel=0.0

class Mapa():    ###Mapa de features
    def __init__(self):
        self.conos=[]
        self.deteciones=[]

        self.track_azul=[]
        self.track_amarillo=[]

    def add_detecion(self,x,y,t,t_inv):
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

        candidato_detecion=Detecion()
        candidato_detecion.x=point_source.point.x #Cordenada x
        candidato_detecion.y=point_source.point.y #Cordenada y
        candidato_detecion.x_rel=x #Cordenada x rel al coche
        candidato_detecion.y_rel=y #Cordenada y rel al coche [x>0 azul izquierda] [x<0 amarillo derecha]

        #Solo considerar nueva deteion si esta a mas de 1 cm
        encontrado=False
        for detecion in self.deteciones:
            if(distancia(detecion.x,detecion.y,candidato_detecion.x,candidato_detecion.y)<0.01):
                encontrado=True
                break

        if not encontrado:
            self.deteciones.append(candidato_detecion)

        ###Longitud de la lista de detecione determina el tamaño del mapa
        ###200 para competi 500-1000 para test con odom perfecta
        ###1500 o mas para skid pad
        long_list_deteciones=1000
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
        ##Esto habria que optimizarlo
        labels = clust_model.fit_predict([(detecion.x,detecion.y) for detecion in self.deteciones]) ##No incluir y_rel en clustering

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
            x_rel_avr=0.0
            for detecion in deteciones_cono:
                x_avr=x_avr+detecion.x
                y_avr=y_avr+detecion.y
                x_rel_avr=x_rel_avr+detecion.y_rel
            c=Cono()
            c.x=x_avr/len(deteciones_cono)
            c.y=y_avr/len(deteciones_cono)

            if x_rel_avr/len(deteciones_cono)>0:
                c.color='Azul'
            else:
                c.color='Amarillo'

            self.conos.append(c)

    def generar_trazas(self,t,t_inv):
        ###Generar referencias para empezar cadena de trazas
        ref_azul=-1
        ref_amarillo=-1

        for (i,cono) in enumerate(self.conos):
            point_source = Point(x=cono.x, y=cono.y, z=0.0)
            point_source=do_transform_point(geometry_msgs.msg.PointStamped(point=point_source),t_inv)

            c_x=point_source.point.x
            c_y=point_source.point.y
            #if c_x<0:
                #continue

            ###Elige conos mas cercanos a cada lado del coche. Esos se toman como referencia
            if c_y>0: #Azul
                if ref_azul==-1:
                    ref_azul=i
                else:
                    c_r_x=self.conos[ref_azul].x
                    c_r_y=self.conos[ref_azul].y
                    if distancia(t.transform.translation.x,t.transform.translation.y,cono.x,cono.y)<distancia(t.transform.translation.x,t.transform.translation.y,c_r_x,c_r_y):
                        ref_azul=i

            else: #Amarillo
                if ref_amarillo==-1:
                    ref_amarillo=i
                else:
                    c_r_x=self.conos[ref_amarillo].x
                    c_r_y=self.conos[ref_amarillo].y
                    if distancia(t.transform.translation.x,t.transform.translation.y,cono.x,cono.y)<distancia(t.transform.translation.x,t.transform.translation.y,c_r_x,c_r_y):
                        ref_amarillo=i

        if ref_azul==-1 or ref_amarillo==-1:
            return -1 #Error si no se pueden encontrar referencias

        self.conos[ref_azul].color='ref'
        self.conos[ref_amarillo].color='ref'

        link_azul=-1
        for (i,cono) in enumerate(self.conos):
            point_source = Point(x=cono.x, y=cono.y, z=0.0)
            point_source=do_transform_point(geometry_msgs.msg.PointStamped(point=point_source),t_inv)

            c_x=point_source.point.x
            c_y=point_source.point.y
            if c_x<0:
                continue

            if c_y>0: #Azul
                if link_azul==-1:
                    link_azul=i
                else:
                    c_r_x=self.conos[link_azul].x
                    c_r_y=self.conos[link_azul].y
                    if distancia(self.conos[ref_azul].x,self.conos[ref_azul].y,cono.x,cono.y)<distancia(self.conos[ref_azul].x,self.conos[ref_azul].y,c_r_x,c_r_y):
                        link_azul=i
            else: #Amarillo
                pass

        self.conos[link_azul].color='ref'

        ###Completar track