# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 19:24:02 2024

@author: Я
"""

print ('Math 3')
x= float(input('x= '))
y= float(input('y= '))
z= float(input('z= '))
for i in range (10, 110,10):
    a=x**2*y**3*z*i
    b=x**3*y**2*z**4*i**2
    c=z*y*x**2*i**3
    print (a,b,c)
print ('End')
input ('Press Enter')
