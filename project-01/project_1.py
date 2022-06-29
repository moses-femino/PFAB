from random import randint

coupon = randint(10,30)
sales_tax = randint(6,13)

product = ""
item_list = []
while product != "Done":
    product = input("Please enter an item(SKU, description, unit price, quantinty) or Done ")
    item = product.split(",")
    #print(product)
    if product != "Done":
        #print(item)
        new_product = {}
        new_product["sku"] = item[0]
        new_product["description"] = item[1]
        new_product["unit_price"] = item[2]
        new_product["quantity"] = item[3]
        item_list.append(new_product)

print(item_list)

subtotal = 0 
for item in item_list:
    print(item)
    #multiply unit_price by quantity for each item and add
    price = float(item["unit_price"]) * int(item["quantity"])
    subtotal = subtotal + price
print("Your subtotal is $" + str(subtotal))


""" print("Shopping complete")
print(item_list)
print("Congratulations! You have recieived a coupon that will save you " + str(coupon) + "%!")
print("The sales tax on your order is " + str(sales_tax) + "%.")
#print("Your subtotal after the discount is " )
#print("Your subtotal before taxes is ")
#print("Your total after all discounts and taxes is ")
print("Thank you for shopping with us! Have a great day :)")
 """