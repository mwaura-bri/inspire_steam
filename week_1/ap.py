# This is a program the helps determines the arithmetic progression of a sequence
# Date : 20/02/2-24
# Name : Bridgett Mwaura

a = int(input("enter the first term :"))
d = int(input("enter the common difference :"))
n = int(input("enter the number of terms :"))

sum = 0
term = a

for i in range(n):
    print(term,end =" ")
    sum+= term
    term+= d

    print("\n the sum of the arithmetic progression is ", sum)

