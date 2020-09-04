# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 18:13:01 2020

@author: Marta1
"""

""" Ejemplo de métodos público y privado"""

class Ejemplo:
    def publico(self):
        print("publico")
    def __privado(self):
        print("privado")
        
ej= Ejemplo()
ej.publico()
ej._Ejemplo__privado()