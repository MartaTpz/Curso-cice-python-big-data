# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 18:26:36 2020

@author: Marta1
"""

"""Getters y setters"""

class Fecha():
    def __init__(self):
        self.__dia= 1
    def getdia(self):
        return self.__dia
    def setdia(self, dia):
        if dia >0 and dia<31:
            self.__dia=dia
        else:
            print("Error")
    dia= property(getdia, setdia)
fecha1= Fecha()
fecha1.dia=34