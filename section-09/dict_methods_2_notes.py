ex_1 = {}.fromkeys(["address"], "1600 Pennysylvania Avenue NW")
print(ex_1)
#use of the .fromkeys() method

ex_2 = {}.fromkeys("ad", "1600 Pennysylvania Avenue NW")
print(ex_2)
#using an iterable and list example

ex_3 = {"make": "Honda", "model": "civic", "year": 2016}
ex_3.pop("model")
print(ex_3)
#use of the .pop() method

ex_4 = {"make": "Honda", "model": "civic", "year": 2016}
popped = ex_4.pop("model")
print(ex_4)
print(popped)
#returns the value of the key value pair 

ex_5 = {"name": "bob", "age": 38, "occupation": "accountant", "workplace": "H&R block"}
ex_5.popitem()
print(ex_5)
#use of .popitem() method