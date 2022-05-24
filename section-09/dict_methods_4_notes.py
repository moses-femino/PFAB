computers = {"Google": "ChromeBook", "Apple": "MacBook", "Microsoft": "Surface Pro"}

if "Lenovo" not in computers:
    computers["Lenovo"] = "ThinkPad"

print(computers)

computers.setdefault("Lenovo", "ThinkPad")
#use of the .setdefault() method

computers.setdefault("Lenovo", "IdeaPad")
print(computers)
#if you use set default it doesn't change from the original 

empty = dict()
print(empty)
with_values = dict(a=1, b=2, c=3)
print(with_values)
#use of dict() method