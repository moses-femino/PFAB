from random import randint

fuel = randint(10, 25)
miles = randint(200, 400)

print("The car can travel " + str(miles // fuel)  + " miles per gallon.")
print("The car's fuel tank can hold " + str(fuel) + " gallons.")
print("The car can travel " + str(miles) + " miles on a full tank.")
#miles per gallon programming challenge