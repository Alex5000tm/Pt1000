# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 20:16:46 2024

@author: Я
"""
import random
print ('Game Number 1.0')
random.seed(70)
c= random.randint(0,10)
print ('Enter number?')
d=int (input())
if (d==c):
    print ('Win!')
else:
    print ('Loose!')
print ('Game over!!!')
input()

