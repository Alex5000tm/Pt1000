# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:00:18 2024

@author: Я
"""

from math import cos, sin, sqrt
print ('Math_3_SK_507')
a= float (input ('a= '))
b= float (input ('b= '))
c= float (input ('c= '))
for i in range (0,110,10):
    x=cos(a*b*c*i)
    y=sin(a*b*c*i)
    z=sqrt(a*b*c*i)
    print (i,x,y,z)
print ('__End__')
input()