planets = ["pluto", "mars", "earth", "venus"]
del planets[0]
print(planets)
#use of the delete method 


planets_1 = ["pluto", "mars", "earth", "venus"]
planets_1.remove("pluto")
print(planets_1)

colors = ["blue", "red", "white", "blue", "orange", "blue"]
colors.remove("blue")
print(colors)
#use of the .remove method... it only removes the first string if there are multiple of the same one


pets = ["cat", "dog", "parrot"]
print(pets)
pets.append("fish")
print(pets)
# use of the .append method


pets_1 = ["cat", "dog", "parrot"]
pets_1.insert(1, "turtle")
print(pets_1)
#use of the .insert method


num_list = [2.718, 4, -19, 10000, 0]
print(num_list)
num_list.sort()
print(num_list)

str_list = ["Ringo", "John", "George", "Paul"]
print(str_list)
str_list.sort()
print(str_list)

num_list_1 = [2.718, 4, -19, 10000, 0]
str_list_1 = ["Ringo", "John", "George", "Paul"]
num_list_1.sort(reverse=True)
print(num_list_1)
str_list_1.sort(reverse=True)
print(str_list_1)

mixed = [False, 5.67, -2]
mixed.sort()
print(mixed)

ASCIIbetical = ["Andy", "kiwi", "apple", "Karen", "Brian", "banana"]
ASCIIbetical.sort()
print(ASCIIbetical)

ASCIIbetical_1 = ["Andy", "kiwi", "apple", "Karen", "Brian", "banana"]
ASCIIbetical_1.sort(key=str.lower)
print(ASCIIbetical_1)
#uses of the .sort method... .sort method can't be used with strings and numbers but it can be used with boolean values and numbers because false is assigned 0 and true is assigned 1.
#python doesn't use alphabetical order but uses ASCIIbetical order... if a word is lower case it will be pushed to the end of the sort and the lower case strings get sorted
#unless you use key=str.lower


metals = ["copper", "gold", "silver", "iron"]
print(metals.index("silver"))
#use of the .index method 


bands = ["Queen", "Led Zeppelin", "The Beatles", "MUSE", "Radiohead"]
end = bands.pop()
print(bands)
print(end)

bands_1 = ["Queen", "Led Zeppelin", "The Beatles", "MUSE", "Radiohead"]
end_1 = bands_1.pop(3)
print(bands_1)
print(end_1)
#uses of the .pop method