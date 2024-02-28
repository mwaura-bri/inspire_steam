# friends
friends=["Faith","Renish","Wayne","Michael","Mercy"]
for friend in friends :
    print(friend)



enemies=friends[:] # to copy one list in another
for enemy in enemies :
    print(enemy)


fruits=["melon","strawberry","avocado" ,"grapes" ,"apple","maongo"]

# slice the list to get part of the list

print(fruits[0:3])


del fruits[0]
print(fruits)

squares=[] # initiates an empty list
for x in range(0,11) :
    squares.append(x**2)

print(squares)    