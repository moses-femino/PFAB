ex_1 = [1, 2, 3]
ex_1[1] = 5
print(ex_1)
ex_2 = "123"
ex_2 = "153"
print(ex_2)

ex_3 = "No, you can't."
ex_4 = "Yes" + ex_3[3:11] + "!"
print(ex_4)

ex_5 = 3.14
ex_6 = "coconut"
ex_7 = ex_5
ex_8 = ex_6
print(ex_7)
print(ex_8)
#can't do this with lists

ex_9 = [1, 2, 3, 4, 5]
ex_10 = ex_9
ex_10[2] = 4
print(ex_9)
print(ex_10)
#gets messed up because they reference the same list

import copy
ex_11 = [1, 2, 3, 4, 5]
ex_12 = copy.deepcopy(ex_11)
ex_12[2] = 4
ex_13 = ex_12
ex_13[4] = 6
print(ex_11)
print(ex_12)
#deep copy function

ex_14 = ["bush",
          "fern",
          "tree",
          "moss"]

print(ex_14)
#line list continuation

ex_15 = 2 + \
        4 + \
        1

print(ex_15)
#line continuation character... when doing math it is essential to line up the numbers

ex_16 = "The Emp\
ire Strikes Back"

print(ex_16)
#line continuation character... with strings you don't have to line it up

ex_17 = "hello " + \
        "world"

print(ex_17)
#line continuation character on a concatenated string