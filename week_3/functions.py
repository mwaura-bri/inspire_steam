
# define the function
def print_name():
    print("my name is Bridgett Mwaura")




# calling the function
print_name()    
print_name() 
print_name() 
print_name() 
print_name() 


# parametus
def print_details(name , age, ID , gender) :
    print("i am{0},{1}years old,my ID no is{2} and gender is{3}".format(name , age, ID , gender))


print_details("Bridgett Mwaura" , "18", "21933530" , "female")    
print_details("Mercy Muthoni" , "18", "22444573" , "female")

def sum_nums(x,y) :
    return x + y

z = sum_nums(10,20)
print(z)

def prod_nums(x,y) :
    return x * y

print(prod_nums(5,16)) 

def print_odds(first_num,last_num) :
    for i in range (first_num , last_num) :
        print(i % 2)


print_odds(0,19) 