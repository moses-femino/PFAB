print("hello world".rjust(15))
print("hello world".ljust(15) + "four spaces later.")
print("hello world".rjust(15, "-"))
print("hello world".ljust(15, "*"))
print("hello world".center(15))
print("hello world".center(15, ":"))
#uses of the .rjust, .ljust, and .center methods


print("I had an exciting trip!!!11111")
print("I had an exciting trip!!!11111".strip("1"))
print("I had an exciting trip!!!11111".rstrip("1"))
print("I had an exciting trip!!!11111".lstrip("1"))
#example of .strip, .rstrip, .lstrip methods


print("juice, bread, cheese, beef, bread".rstrip(", bread"))
print("juice, bread, cheese, beef, bread".rstrip(", ed arb "))
print("blueblueyellowblue".strip("eulb"))
#shows that strip can remove letters as well as full string. 


print("Good morning.".replace("morning", "afternoon"))
#use of the .replace method