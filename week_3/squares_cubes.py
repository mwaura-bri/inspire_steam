# this is a program used to find the squares and cubes of numbers 
# date : 29/02/2024
# name : Bridgett Mwaura

numbers = [1,2,3,4,5,6,7,8,9,10]

squares = [numbers ** 2 for numbers in numbers]
cubes = [numbers ** 3 for numbers in numbers]

print("numbers : " , numbers)
print("squares : " , squares)
print("cubes :" , cubes)