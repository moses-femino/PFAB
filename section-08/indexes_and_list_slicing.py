indexes_example = ["carpet", "hardwood", "linoleum"]
print(indexes_example[1])
#allows you to print the string that is at index 1


indexes_example_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(indexes_example_1[2][0])
print(indexes_example[2][0])
#you can print a number from the whichever lists index and then the number inside the list 


negative = [1, 2, 3, 4, 5]
print(negative[-1])
print(negative[-2])
print(negative[-3])
print(negative[-4])
print(negative[-5])
#can use negative numbers to find certain numbers in an index(goes backwards almost)


mixed = [False, 365, 4.24, "this is a string"]
print(mixed[2] + 1.76)
print("I have used \"" + mixed[-1] + "\" as an example too many times.")
#can use math opperators to add either numbers or create sentences just to name a few


sliced = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sliced[:4])
print(sliced[3:8])
print(sliced[6:])
#different ways to use slices


example = [2, 4, 6, 8, 0]
print(example)
example[3] = 10
print(example)
#can add values to a list to replace values


example_1 = [2, 4, 6, 8, 0]
print(example_1)
example_1[1:4] = [3, 2, 1]
print(example_1)
#another way to add to a list

example_2 = [2, 4, 6, 8, 0]
print(example_2)
example_2[4:7] = [7, 6, 5]
print(example_2)
#another way to add to a list