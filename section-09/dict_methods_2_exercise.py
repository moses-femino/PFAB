from multiprocessing.sharedctypes import Value


consonants = {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant")
for key, value in consonants.items():
    print(key, value)

fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
mcdonald = fast_food_items.pop("McDonald's")
print(mcdonald)

fast_food_items.popitem()
print(fast_food_items)
