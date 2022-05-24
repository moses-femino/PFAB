ex_1 = {1: "England", 2: "Scotland", 3: "Wales", 4: "Northern Ireland"}
print(ex_1)
ex_1.clear()
print(ex_1)
#use of the .clear() method

birth_years = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
print(birth_years)
people = birth_years.copy()
people[1982] = "madeline"
print(birth_years)
#use of the .copy() method

city_info = {"country": "Canada", "province": "Ontario", "city": "Toronto"}
population = {"population": 2930000}
city_info.update(population)
print(city_info)
print(population)
#use of the .update() method