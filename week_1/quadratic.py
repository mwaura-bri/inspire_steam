# program to solve the quadratic equations
# Date : 20/02/2024
# Name : Bridgett Mwaura
import math
a=float (input("enter the coefficient of first term :"))
b=float(input("enter the coeffiecient of second term :"))
c=float(input("enter the coeffiecient of third term :"))



d=(b**2) - (4 *a *c)

x_1= (-b +math.sqrt(d)) / (2* a)
x_2= (-b - math.sqrt(d)) / (2* a)

print("the solution of the quadratic equation is",x_1)
print("the solution of the quadratic equation is",x_2)