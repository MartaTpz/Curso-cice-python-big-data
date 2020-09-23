# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 00:39:15 2020

@author: Marta1
"""

#llamando a una funcion

def suma(val1=0, val2=0):
    return val1+val2

def operacion(funcion, val1=0, val2=0):
    return funcion(val1,val2)


funcion_suma= suma

funcion_operacion=operacion(funcion_suma, 10, 20)   
print(funcion_operacion)


print("\n") 

my_string= '''holaaa
aaa
aaa
'''

print(my_string)