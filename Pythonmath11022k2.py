from math import cos,sin,pi,acos,asin,cosh,sinh
a=2
b=3.1425713
d=float(input('d= '))
x=cos(a*b*d**2)/sin(b**2*a**2/d)/pi
y=acos(0.357)*b/a/pi
z=asin(0.574)*b**3/a/pi
r=cosh(d*b/a)*sinh(d*b**2/a)/pi
print (x,y,z,r)
print ('CN= ', x+y+z+r)
input()
