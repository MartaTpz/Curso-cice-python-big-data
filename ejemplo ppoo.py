# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 14:17:00 2020

@author: Marta1
"""

class Vehículo:
    """Esta es la clase vehículo que define las características 
    de cualquier vehículo. A continuación las ponemos"""
    
    def __init__(self,acolor,aancho,avelocidad,aplazas):
        #los objetos de la clase vehículo tienen cuatro atributos
       self._color=acolor
       self._ancho=aancho
       self._velocidad=avelocidad
       self._plazas=aplazas
       
    #Resto de métodos
    
    def cambiarcolor(self, nuevocolor):
        self._color=nuevocolor
        
        
    def parar(self):
        self._velocidad= 0
        
vrojo= Vehículo("rojo", 3, 400, 2)
vverde= Vehículo("verde", 2, 200, 4)
vazul= Vehículo("azul", 1, 100, 2)
