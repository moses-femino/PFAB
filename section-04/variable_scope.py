example = "hello world"  #global


def loc_ex():
    example = "this is a string"  #local
    return example


print(example)
print(loc_ex())


def loc_ex_1():
    breakfast = "waffles"
    return breakfast

loc_ex_1()
print(breakfast)
#local variables cannot be used by code in the global scope


def print_glob():
    loc_var = " that is very long."
    print(glob_var + loc_var)

glob_var = "This is a string"
print_glob()
#global variables can be accessed by code in a local scope



def first():
    loc = 2
    return loc

first()
second()
#the local scope of one function can't use variables from another function's local scope


def loc_ex_2():
    fruit = "pear"
    print(fruit)

def loc_ex_3():
    fruit = "banana"
    print(fruit)

fruit = "apple"
loc_ex_2()
loc_ex_3()
print(fruit)
#you can use the same name for different variables as long as they are in different scopes


def loc_ex_4():
    global fruit
    fruit = "pear"
    print(fruit)


fruit = "apple"
loc_ex_4()
print(fruit)
#global statement