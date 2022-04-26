number = int(input("Enter a number"))


def factorial(number):
    product = 1
    while number > 0:
        product *= number
        number -= 1
    return product

print("The factorial of " + str(number) + " is " + str(factorial(number)))