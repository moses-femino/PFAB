#a set is a data type that consists of a collection of items, much like a list
#There are 2 key differences... they cannot have duplicate values in them and the items they contain are unordered

set_1 = {9, 8, 7, 6}
set_2 = set({"a", "b", "c", "d", "e"})
print(set_1)
print(set_2)
#the two basic ways to create sets... use curly brackets or use the set function
#if you want to create an empty set that you can change later, you have to use the set function

set_3 = set(range(1, 12, 2))
print(set_3)
#passing the set function a call of the range function as an argument... the range will be turned into a set
#this example gets all of the odd positive integers from 1 to 12 using a range

set_4 = {"a", 3.14, 18, True}
print(set_4)
#sets can hold items that are of different data types

set_5 = {3, 6, 9, 12, 15}

for num in set_5:
    print(num)
#unlike lists or tuples, sets can't have their items accessed from them by index... have to use a loop

print(12 in set_5)
#use in to check if an item is in a set