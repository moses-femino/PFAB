major_cities = ("Tokyo", "London", "Boston", "Shanghai", "Sydney")

for city in major_cities:
    print(city)
#printing the items of a tuple using a for loop

count = 0
while count < len(major_cities):
    print(major_cities[count])
    count += 1
#iterating through the tuple using a while loop

backwards = len(major_cities) - 1
while backwards >= 0:
    print(major_cities[backwards])
    backwards -= 1
#using a while loop to iterate backwards

ints =  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(ints[::3]) #stride length of 3
print(ints[1::2]) #evens only
print(ints[7::-1]) #backwards from 8
print(ints[8::-2]) #odds only backwards
#tuple slicing with step
