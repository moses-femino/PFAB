#data type made up of a collection of items
#Unlike lists, they are enclosed in parentheses instead of square brackets

tuple_1 = ("a", "b", "c", "d", "e" )
tuple_2 = (2.718, False, [1, 2, 3])
tuple_3 = (1, 1, 0, 0, 0)
#example tuples... can contain the same or different data types and also have multiple instances of a data type

tuple_4 = (5, 4, 3, 2, 1)
tuple_5 = tuple([3.14, 2.205, 10])
tuple_6 = tuple("edcba")
print(tuple_5)
print(tuple_6)
#can create a tuple manually or use the tuple function

tuple_7 = tuple({"a": 1, "b": 2, "c": 3})
print(tuple_7)
#no point in using a dictionary because only the key is made into a tuple

tuple_8 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple_8[2])
print(tuple_8[:8])
print(tuple_8[2:7])
print(tuple_8[3:])
#each item in a tuple has an index number so you can access values by index or slice like lists or strings!
#slicing uses same syntax as the slicing of lists and strings... when a tuple is sliced the resulting slice is also a tuple


tuple_9 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tuple_9[0] = "a"
#tuples are an immutable data type which means they cannot be changed

#tuples have smaller memory and take up less space then lists