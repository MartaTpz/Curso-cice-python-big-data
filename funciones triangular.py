# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 18:04:19 2020

@author: Marta1
"""

def triang_1(n):
    a=[]
    for i in range(n):
       a.append(i*(i+1)/2)
    return a

def triang_2(n):
    a=[0]
    for i in range(1,n):
        a.append(a[i-1]+i)
    return a
print(triang_1(15))