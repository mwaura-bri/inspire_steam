# This is a program for calculating the volume of a cylinder
# Date : 20/02/2024
# Name : Bridgett Mwaura

import math

radius = float(input("enter the radius of the cylinder: "))
height = float(input("enter the height of the cylindrr: "))

cylinder_volume = math.pi * radius ** 2 * height
print("the volume of the cylinder is",cylinder_volume)