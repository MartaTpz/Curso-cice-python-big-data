# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 13:10:24 2020

@author: Marta1
"""

i=-2
while i<4:
    i+=1
    print(i)
print('Estoy fuera del bucle')

i=0
while i <5:
    print(i)
    i+=1
    if i==3:
        break
    
precio= 10/3
print(precio)

talla= 42
print('Tengo la talla %d' % talla)
print('En %d meses quiero pesar %.2f menos' % (2, 2.500000))
print('La suma de {0} con {1} es: {2}'.format(1,3,4))
print('si un kilo de tomates cuesta {0} € medio cuesta {1:.2f} '.format(3,3/2))