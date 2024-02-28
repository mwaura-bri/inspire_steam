my_laptop={"make":"probook","colour":"grey","weight":"2.0","year":"2024","storage":"256GB"}
print(my_laptop)


print(my_laptop["make"])
print(my_laptop["colour"])
print(my_laptop["storage"])
print(my_laptop["year"])
# to change values
my_laptop["colour"] = "red "
my_laptop["year"] = "2009"
print(my_laptop)

my_laptop["size"]="1200mm x600mm"
print(my_laptop)

del my_laptop["colour"]


print(my_laptop)

size_laptop = my_laptop.copy


for key,value in my_laptop.items() :
    print(key)
    print("\n")
    print(value)






