# This is a program used to spawn the terms and sum in geometric progression
# Date : 20/02/2024
# Name : Bridgett Mwaura

a =int(input("enter the first term :"))
r =int(input("enter the common ratio:"))
n =int(input("enter the number of terms :"))

sum = 0
term = a

for i in range(n):
    print(term,end=" ")
    sum+= term
    term*=r
    print("\n the sum of the geometri progression is",sum)



