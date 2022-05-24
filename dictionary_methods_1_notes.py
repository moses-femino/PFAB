birth_years = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}

print(birth_years.keys())
#use of the .keys() method

for key in birth_years.keys():
    print(key)
#using a for loop to itirate through what is returned

print(birth_years.values())
#use of the .values() method

for value in birth_years.values():
    print(value)
#using a for loop to itirate through what is returned

print(birth_years.items())
#use of the .items() method

for key, value in birth_years.items():
    print(key, value)
#itirating through the tuples that get returned

print(list(birth_years.keys()))
print(list(birth_years.values()))
print(list(birth_years.items()))
#how to print the methods using list

print("elizabeth" in birth_years.values())
#example use of the in operator 

if 1975 in birth_years:
    print(birth_years[1975])
else:
    print("1975 is not a key in birth_years.")

print(birth_years.get(1975, "1975 is not a key in birth_years."))
#use of .get()

print(birth_years)
people = birth_years
people[1982] = "madeline"
print(birth_years)
#example of replacing a value in a dictionary 