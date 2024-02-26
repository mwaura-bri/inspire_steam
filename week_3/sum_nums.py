# This is a programme the gets the sum of the first twenty numbers
# Date : 26/02/2024
# Name : Bridgett mwaura

sum_nums=0
for x in range(0,21):
    max_value=int(input("enter the maximum number"))
    for x in range(0,max_value +1):
        sum_nums=sum_nums + x
        print(sum_nums)
