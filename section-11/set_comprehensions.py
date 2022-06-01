#third and slightly more advanced way to make a set

comp_1 = {even+2 for even in range(2, 11, 2)}
print(comp_1)
#3 things that make up a set comprehension
#entire thing must be enclosed in curly brackets to signal to Python that it's a set
#there is a for loop that goes over an iterable data type
#there is an action that is done to each item that the for loop iterates over 

comp_2 = {char.lower() for char in "ALLCAPS"}
print(comp_2)
#set comprehension example involving a string with repeats 
#set's can't have repeats so values will only appear once if there are multiple instances 