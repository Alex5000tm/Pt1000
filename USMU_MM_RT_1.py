from math import cos, sin, sqrt, pi
import time
import random
print('USMU_MM_RT_1')
a=float(5.78)
b=float(7.778)
c=float(2.145)
for i in range (-200,200,20):
    d=random.randrange(-50,50)
    e=cos(a*b*c)-sin(a*b*c)*i*d
    print(i,d,e)
    time.sleep(1)
print('End')
input('Press any key for exit...')
