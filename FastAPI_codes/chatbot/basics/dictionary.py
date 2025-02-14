my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}
print(my_vehicle)

for key in my_vehicle.keys():
    print(key)

my_vehicle2 =my_vehicle

print(my_vehicle2)
my_vehicle2["number_of_tires"]=4
print(my_vehicle2)
my_vehicle2.pop("mileage")
print(my_vehicle2)
print(my_vehicle2.keys())

for x in my_vehicle.keys():
    print(x)

for x,y in my_vehicle.items():
    print(x,y)