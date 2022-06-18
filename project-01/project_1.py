from random import randint

new_product = {}
product = ""
items_list = []
while product != "Done":
    product = input("Please enter an item(SKU, description, unit price, quantinty) or Done ")
    item = product.split(",")
    print(item)
    if product != "Done":
        new_product["sku"] = item[0]
        new_product["description"] = item[1]
        new_product["unit_price"] = item[2]
        new_product["quantity"] = item[3]
        items_list.append(new_product)
    
print("Shopping complete")
print(items_list)



""" objects = input("What quantity of this item do you want to purchase")

coupon = randint(10,30)
sales_tax = randint(6,13)

print("Congratulations! You have recieived a coupon that will save you " + str(coupon) + "%!")
#print("You have purchased ")
#print("Your subtotal after the discount is " )
#print("Your subtotal before taxes is ")
#print("Your total after all discounts and taxes is ")
#print("Thank you for shopping with us! Have a great day :)")
 """