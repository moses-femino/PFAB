import random

coupon = random.randrange(10,31,5)
sales_tax = random.randint(600,1300) / 100
product = ""
item_list = []

while product != "Done":
    product = input("Please enter an item(SKU, description, unit price, quantinty) or Done ")
    item = product.split(",")

    if product != "Done":
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
    price = float(item["unit_price"]) * int(item["quantity"])
    subtotal = subtotal + price

discounted_subtotal = subtotal * (1 - coupon / 100)
taxed_total = discounted_subtotal * (1 + sales_tax / 100)

print("Shopping complete")
print("Your subtotal is $" + str(subtotal))
print("Congratulations! You have received a coupon that will save you " + str(coupon) + "%!")
print("Your subtotal after the coupon has been applied is $" + str(round(discounted_subtotal, 2)))
print("The sales tax on your order today is " + str(sales_tax) + "%")
print("Your total after coupons and taxes is $" + str(round(taxed_total, 2)))
print("Thank you for shopping with us! Have a great day :)")
 