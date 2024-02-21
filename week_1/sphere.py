# This is a program that is used for calculating the surface area of a sphere
# Date : 20/02/2024
# Name : Bridgett Mwaura

import math

r = float(input("enter the radius of the sphere :"))
surface_area = 4 * math.pi * pow(r, 2)


print("the surface area of the sphere is {:.2f}".format(surface_area))
