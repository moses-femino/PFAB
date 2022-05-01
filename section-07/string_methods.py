all_low = "there are no capitals here."
print(all_low.upper())
print(all_low)

all_up = "THIS IS SHOUTING TEXT!"
print(all_up.lower())
#.upper and .lower methods


print("Mixed Case".isupper())
print("ALL CAPS!".isupper())
#.isupper method


print("AAAHHH!".islower())
print("$100 is a lot to make in an hour.".islower())
#.islower method


print("".isupper())
print("37&8.,?:\"".islower())
#these methods don't work with special cases


print("SHOUT!".lower().isupper())
#this makes "SHOUT!" lower case then checks if the letters are upper which results in a false expression


#.isalpha() checks if the string is only letters
#.isalnum() checks if the string is only numbers and letters
#.isdecimal() checks if the string is only numbers
#.isspace() checks if the string or place holder in the string chosen is only a space(s)
#.istitle() checks if the string follows only titlecase


print(" ".isspace())
print("               ".isspace())
print("not just spaces".isspace())
print("not just spaces"[3].isspace())
#different examples of the .isspace method


print("the great gatsby".title())
#.title makes the first letter in each word of the string upper case


print("this is a string".startswith("this"))
print("this is a string".startswith("t"))
#.startswith is a method that allows you to check if the string beginning matches with the arguement 


print("".join(["one", "two", "three"]))
print(" ".join(["one", "two", "three"]))
print(",".join(["one", "two", "three"]))
print(", ".join(["one", "two", "three"]))
print("...".join(["one", "two", "three"]))
#.join joins together the strings... there are many different ways to use this method


print("Eggs, Milk, Waffles, Bacon".split(", "))
#the .split method splits up the string

