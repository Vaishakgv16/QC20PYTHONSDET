import math
# print(math.sqrt(256))
# print(math.cbrt(27))

#1. WAPT print area of a circle
'''
r=16
area ==pir2
print(math.pi*r**2)
'''
#another way of Importing math module
from math import *
# print(cos(0))
# print(pi)

#2. WAPT area of Triangle
""""
base=eval(input("Enter the Base value"))
height=eval(input("Enter the height value"))
area=1/2*base*height
print("Area of the circle =",area,"sq units")
"""
#3. WAPT area of Rubix Cube
'''
side_length_cube=eval(input("Enter the side length"))
area =6*(side_length_cube)**2
print("Area of the rubix cube =",area,"sq units")
'''
#4. WAPT area of Cylinder
"""
r=eval(input("Enter the radius"))
h=eval(input("Enter the height"))
area=2*pi*r*(r+h)
print("Area of the cylinder =",area,"sq units")
"""
#5. WAPT area of Rectangle
'''
length=eval(input("Enter the length"))
width=eval(input("Enter the width"))
area=length*width
print("Area of the rectangle ",length,"*",width,"=",area,"sq units")
'''
#6. WAPT area of Trapezium
"""
a=eval(input("Enter the parallel base side a"))
b=eval(input("Enter the parallel base side b"))
h=eval(input("Enter the height"))
area=1/2*(a+b)*h
print("Area of the Trapezium =",area,"sq units")
"""
#7. WAPT area of Rhombus
'''
d1=eval(input("Enter the diagonal length d1"))
d2=eval(input("Enter the diagonal length d2"))
area=1/2*d1*d2
print("Area of the Rhombus 1/2 *",d1,"*",d2,"=",area,"sq units")
'''
#8. WAPT area of Semicircle
"""
r=eval(input("Enter the radius"))
area=1/2*pi*r**2
print("Area of the Semicircle 1/2 *",pi,"*",r**2,"=",area,"sq units")
"""
#9. WAPT area of Ellipse
'''
a=eval(input("Enter the length of semi major axis"))
b=eval(input("Enter the length of semi minor axis"))
area=pi*a*b
print("Area of the Ellipse",pi,"*",a,"*",b,"=",area,"sq units")
'''
#10. WAPT area of Parallelogram
b=eval(input("Enter the base"))
h=eval(input("Enter the height"))
area=b*h
print("Area of the Parallelogram",b,"*",h,"=",area)

