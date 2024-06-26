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

###Utils###
def distancia(x_c,y_c,x,y):         ###Distancia entre dos deteciones
    return numpy.sqrt((x_c-x)**2 + (y_c-y)**2)

def unit_vector(vector):
    return vector / numpy.linalg.norm(vector)

def angle(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return numpy.arccos(numpy.clip(numpy.dot(v1_u, v2_u), -1.0, 1.0))

###Objetos de datos####

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

###Logica del mapa###

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
                x_rel_avr=x_rel_avr+detecion.y_rel  ###Revisar No se pueden usar mediciones relativas
            c=Cono()
            c.x=x_avr/len(deteciones_cono)
            c.y=y_avr/len(deteciones_cono)

            c.color='ns'

            self.conos.append(c)

    def generar_track(self,track,t,t_inv,color):
        terminar=0 ##Para asegurar que no sigue hasta el infinito
        while True:
            terminar=terminar+1  #En teoria nunca se ejecuta
            if terminar>20:
                print("terminando")
                break

            #Generar referencias con respecto al coche
            #Esto solo se utiliza para ver a que lado del coche esta el cono y decidir asi su color
            link=-1
            point_source = Point(x=track[-1].x, y=track[-1].y, z=0.0)
            point_source=do_transform_point(geometry_msgs.msg.PointStamped(point=point_source),t_inv)
            c_x_r=point_source.point.x
            c_y_r=point_source.point.y
            
            for (i,cono) in enumerate(self.conos):
                #Solo admitir conos que son candidatos
                #Es decir:
                #1. Estan a entre 0.5 y 6 metros del anterior. Max FS es 5m
                #2. Se encuentran en un abanico de +-60grados orientado segun los dos anterioires conos.
                d=distancia(track[-1].x,track[-1].y,cono.x,cono.y)
                if d>6 or d <0.5:
                    continue
                if len(track)>=2:
                    a=angle((track[-2].x-track[-1].x,track[-2].y-track[-1].y),(track[-1].x-cono.x,track[-1].y-cono.y))
                    if a <-0.7 or a >0.7: #+-40grados
                        continue
                else:  #Si no hay suficientes datos para los criterios anterioires. Se aplican criterios especificos a cada lado del coche
                    point_source = Point(x=cono.x, y=cono.y, z=0.0)  #Cambiar al sistema de referencia del coche
                    point_source=do_transform_point(geometry_msgs.msg.PointStamped(point=point_source),t_inv)
                    c_x=point_source.point.x
                    c_y=point_source.point.y
                    if color=='Azul':
                        if c_x<c_x_r+0.1 or c_y<0:
                            continue
                    elif color=='Amarillo':
                        if c_x<c_x_r+0.1 or c_y>0:
                            continue
                    else:
                        print("Color no conocido")

                repe=False
                for c in track:  #Comprobamos que el cono no este ya en el track
                    if distancia(c.x,c.y,cono.x,cono.y)<0.01:
                        repe=True
                        break
                if repe:
                    continue

                #Si el cono a sido aceptado. Se comprueba si es el mas cercano de los procesados
                if link==-1:
                    link=i  #Si no hay suficientes conos no hace falta el abanico y no se puede hacer entonces no se hace
                else:
                    if distancia(track[-1].x,track[-1].y,cono.x,cono.y)<distancia(track[-1].x,track[-1].y,self.conos[link].x,self.conos[link].y):
                        link=i

            if link==-1:
                break

            self.conos[link].color=color
            track.append(self.conos[link])

        return track

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
            print("No se encontraron referencias")
            return -1 #Error si no se pueden encontrar referencias

        #Añadir referencia a track azul
        self.conos[ref_azul].color='ref'
        self.track_azul=[]
        self.track_azul.append(self.conos[ref_azul])

        #Añadir referencia a track amarillo
        self.conos[ref_amarillo].color='ref'
        self.track_amarillo=[]
        self.track_amarillo.append(self.conos[ref_amarillo])
        
        self.track_azul=self.generar_track(self.track_azul,t,t_inv,'Azul')
        self.track_amarillo=self.generar_track(self.track_amarillo,t,t_inv,'Amarillo')

        #Si la ultima conexion es compatida eliminar la peor
        #En los ultimos conos hay tendencia a que ambos tracks coincidan porque pueden no haberse detectado todavia los conos de un lado
        if distancia(self.track_azul[-1].x,self.track_azul[-1].y,self.track_amarillo[-1].x,self.track_amarillo[-1].y)<0.01:
            if distancia(self.track_azul[-2].x,self.track_azul[-2].y,self.track_azul[-1].x,self.track_azul[-1].y)>distancia(self.track_amarillo[-2].x,self.track_amarillo[-2].y,self.track_amarillo[-1].x,self.track_amarillo[-1].y):
                self.track_azul.pop()
            else:
                self.track_amarillo.pop()

        track=self.track_azul
        print("Track:")
        for i in range(2,len(track)):
            a=angle((track[i-2].x-track[i-1].x,track[i-2].y-track[i-1].y),(track[i-1].x-track[i].x,track[i-1].y-track[i].y))
            print((track[i].x,track[i].y,a))
        print("Fin track")