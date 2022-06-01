nested = (1, 2, 3, (4, 5, 6), (7, 8, 9), (10, 11, 12))
print(nested[4])
print(nested[5][1])
#nested tuples are a singular or multiple tuples within another tuple
#example of accessing a value from the nested tuple 

repeat = (7, 3, 3, 3, 0, 0, 7, 0, 0)
print(repeat.count(7))
print(repeat.count(3))
print(repeat.count(0))
#example of the .count() method

ints = (1, 1, 7)
print(ints.index(7))
print(ints.index(1))
#example of the .index() method... if there are multiple instances of the same value the index number of the first time the value appears will be returned