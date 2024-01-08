# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 14:12:53 2024

@author: Я
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 19:24:02 2024

@author: Я
"""
from math import cos, sin, sqrt

print ('Math 4')
x= float(input('x= '))
y= float(input('y= '))
z= float(input('z= '))
for i in range (10, 110,10):
    a=cos(x**2)*y**3*z*i
    b=sin(x**3)*y**2*z**4*i**2
    c=sqrt(z)*y*x**2*i**3
    print (i,a,b,c)
print ('End')
input ('Press Enter')
