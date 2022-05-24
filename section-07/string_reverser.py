user_string = input("Enter a string.")
reversed_string = ""

for num in range(len(user_string) - 1 ,-1,-1):
    reversed_string += user_string[num]

print(reversed_string)
