# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 14:24:15 2020

@author: Marta1
"""

def farengtocentig(gradosF):
    return (gradosF-32) * 5/9
lista=list(range(0,130,10))
for gradosF in lista:
    gradosC= farengtocentig(gradosF)
    print('%d ºC =%.1f F' % (gradosF, round(gradosC)))
    