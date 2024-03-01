# this is a program used to calculate prime numbers
# date : 24/02/2024
# name : Bridgett Mwaura

lower = 1
upper = 99

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)