# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:59:15 2020

@author: Marta1
"""

ciudades={'Madrid', 'Sevilla', 'Bilbao'}
for (i, valor) in enumerate(ciudades):
    print('%d: %s' %(i, valor))



#ciudades={'Madrid', 'Sevilla', 'Bilbao'}

    
def media(lista):
        numero=0
        suma=0
        for i in lista: 
            suma+=i
            numero+=1
            media=suma/numero
      
        return media
        
print(media(lista=[1,2]))

    
def media(lista):
      
      
        return sum(lista)/len(lista)
        
print(media(lista=[1,2,3,6,8,9]))