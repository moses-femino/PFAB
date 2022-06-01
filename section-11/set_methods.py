scifi = {"star trek", "star wars", "halo"}
scifi.add("mass effect")
print(scifi)
#use of the .add() method... takes an item of any data type as it's argument and adds that to the set it is called on

fruits = {"apple", "orange", "banana", "tomato"}
fruits.remove("tomato")
print(fruits)
#use of the .remove() method... takes one argument of any data type and removes it from the set it is called on
#does give an error message if you try to remove something that isn't in the set

fruits.discard("pear")
#use of the .discard() method... does the same as remove and also takes on argument 
#doesn't give an error message if you try to remove something that isn't in the set

mountains = {"Everest", "Kilimanjaro", "Fuji"}
print(mountains)
mountains.clear()
print(mountains)
#use of the .clear() method... takes no arguments and just gets rid of everything in the set it is called on

mountains = {"Everest", "Kilimanjaro", "Fuji"}
set_1 = mountains.copy()
print(set_1 is mountains)
print(set_1)
#use of the .copy() method... returns a copy of a set that has it own place in memory
#the copy and the original set are not the same set... even though they have the same values 

set_2 = {1, 2, 3, 4, 5}
set_3 = {6, 7, 8, 9, 10}
set_4 = set_2.union(set_3)
set_5 = set_2 | set_3
print(set_4)
print(set_5)
#use of the .union() method...  allows you to combine all of the items from 2 sets into 1
#can either use .union() or the pipe character | 

set_6 = {4, 5, 6, 7, 8}
set_7 = {6, 7, 8, 9, 10}
set_8 = set_6.intersection(set_7)
set_9 = set_6 & set_7
print(set_8)
print(set_9)
#use of the .intersection() method... allows you to find out what items 2 sets have in common
#can either use .intersection() or an ampersand &

set_10 = set_7 - set_6
print(set_10)

set_11 = set_6.difference(set_7)
print(set_11)
#use of subtraction or the .difference() method