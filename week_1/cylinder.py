# This is a program for calculating the surface area of a cylinder
# Date : 20/02/2024
# Name : Bridgett Mwaura

import math

radius = float(input("enter the radius of the cylinder:"))
height = float(input("enter the height of the cylinder:"))

surface_area = 2 * math.pi * radius * (radius + height)

print("the surface area of the cylinder is",surface_area)