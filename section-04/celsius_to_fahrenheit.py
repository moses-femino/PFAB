celsius = int(input("Enter a number for degrees in celsius."))

def fahrenheit(c):
    return round ((1.8 * c + 32),1)


print ("The fahrenheit equivalent of " + str(celsius) + " degrees celsius is " + str(fahrenheit(celsius)) + ".")
#celsius to fahrenheit problem