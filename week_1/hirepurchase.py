# This is a program tha calculates the hire purchase price
# Date : 20/02/2024
# Name : Bridgett Mwaura


dep = float(input("enter the deposit amount :"))
n =float(input("enter the number of the months :"))
inst =float(input("enter the monthly instalment paid :"))

hpp = dep + (n * inst)
print("the higher purchase price is :", hpp)