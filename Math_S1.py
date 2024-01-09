# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 17:04:18 2024

@author: Я
"""

import os
import math
import time
print ('Math_S1')
a= float (input('a= '))
b= float (input('b= '))
c= float (input('c= '))
print ('proceed...')
time.sleep(2)
x= math.cos(a)*math.cos(b)*math.cos(c)
y= math.sin(a)*math.sin(b)*math.sin(c)
z= math.cos(c)*math.sin(a)*math.cos(b)
print (x,y,z)
time.sleep(12)
input('Press Enter...')
os.system('cls')
print ('End')
input('Press any key')
