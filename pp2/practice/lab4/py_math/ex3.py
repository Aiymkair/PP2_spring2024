from math import *

a = float(input(" Input number of sides:"))
h = float(input("Input the lenght of a side:"))

apophem = h/(2*tan(pi/a))
P = a * h
Area = apophem * P/2
print(f'The area of the polygon is:{round(Area)}')