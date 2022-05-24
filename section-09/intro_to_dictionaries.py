consoles = {"nintendo": "wii", "microsoft": "xbox", "sony": "playstation"}
print(consoles["microsoft"])
#how to access an item in a dictionary

val = consoles["microsoft"]
print(val)
print("The " + consoles["sony"] + " 5 is Sony's newest gaming console.")
#other ways to access an item in a dictionary

mohs_hardness = {9: "corundum", 10: "diamond"}
floats = {1.23: 1000, 3.14159: 10000, 2.718: 100000}
mixed = {"string": 1, 10210: 2, 4.976: 3, False: 4}
#multiple examples of dictionaries

first = {0: 2.1, 1: 2.2, 2: 2.3, 3: 2.4}
second = {2: 2.3, 0: 2.1, 3: 2.4, 1: 2.2}
print(first == second)
#unlike lists, dictionaries are unordered

print(0 in first)
print(1 not in first)
#example use of the in and not in operators
