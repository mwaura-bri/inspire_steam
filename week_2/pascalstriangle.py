# calculating pascals using loops
# date : 22/02/2024
# name : Bridgett Mwaura

from math import factorial

rows = int(input("enter pascals triangle number pattern rows = "))

print("====pascals triangle number pattern====")

for i in range(0, rows):
    for j in range(rows -i + 1):
        print(end = ' ')
    for k in range(0, i + 1):
        print(factorial(i)//(factorial(k) * factorial(i - k)), end= ' ')   
    print()     
