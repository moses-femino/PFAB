from random import randint
shopping_cart = input("Please enter the SKU of the item you would like to purchase")
coupon = randint(10,30)
sales_tax = randint(6,12)

print("Congratulations! You have recieived a coupon that will save you " + str(coupon) + "%!")
#print("Your subtotal after the discount is " )
#print("Your subtotal before taxes is ")
#print("Your total after all discounts and taxes is ")
#print("Thank you for shopping with us! Have a great day :)")
