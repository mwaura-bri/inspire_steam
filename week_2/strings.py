# Strings in python
# Date : 22/02/2024
# Name : Bridgett Mwaura

city = "nairobi"

print(city[0]) # n
print(city[1]) # a
print(city[2]) # i
print(city[3]) # r
print(city[4]) # o
print(city[-1]) # b
print(city[-2]) # i


# Convert to uppercase

print(city)
print("\n") # Prints a new line
print(city.upper())

name ="BRIDGETT"
print(name)
print(name.lower()) # converts print to lower case


town = "    Naivasha   "

print(town)
print("\t") # new tab
print(town.strip())

# add two strings

f_name = "Bridgett"
s_name = "Mwaura"

full_name = f_name + s_name

print(full_name)


# replacing a character

fruit = "orangeooooo"

print(fruit.replace('o' , 'y'))

subject = "physical,sciences"

print(subject.split( "," ))
# printing an integer
age = 18
height = 3.22
print("I am {0} years old and {1} meters tall " .format(age , height))

activity = "dancing"
print("my hobby is %s"%(activity))

height = 1.23
print("my height is %5.3f"%(height))
# printing an integer
age = 18
print("my age is %d"%(age))

name = "BridgettMwaura"
print(len(name))

print(f"my full name is {name}")



school = "engineering"
course = "electrical"

print("i am studying {course}in the school of {school}" . format(course = "medicine", school ="human science"))


