# this is a program used to describe cars
# date : 28/02/2024
# name : Bridgett Mwaura

fav_car={"brand":"Bavarian motors works","colour":"blue","model":"BMW3","speed":"302km/h"}
print(fav_car)

print(fav_car["colour"])
print(fav_car["model"])
print(fav_car["speed"])

# to change the car values
fav_car["colour"] = "black"
fav_car["speed"] = "400km/h"
fav_car["model"] = "BMW 4 Series Gran Coupe"
print(fav_car) 

fav_car["size"] ="4783mm x 1852mm x 1442 mm"
print(fav_car)

del fav_car["model"]
print(fav_car)


for key,value in fav_car.items() :
    print(key)
    print("\n")
    print(value)


