"""  Built-in Dictionary Methods """


#clear the dictionary
d = {'a': 10, 'b': 20, 'c': 30}
d.clear() 

#get the key value
d = {'a': 10, 'b': 20, 'c': 30}
print(d.get("a"))

# if the key is not found in the dictinary the default value will return like kalambayi
print(d.get("mpoyi", "kalambayi"))

# d.items() return list of tuple 
d = {'a': 10, 'b': 20, 'c': 30}
print(d.items())
print(list(d.items())) # return a clean list tuple

# list of all the keys 
print(d.keys())
print(list(d.keys()))# clean list of the keys

# return a list of value 
print(list(d.values()))

#note: Any duplicate values in d will be returned as many times as they occur:

d = {'a': 10, 'b': 10, 'c': 10}
print(list(d.values()))

# remove 

d.pop('b')

# d.popitem() remove the last key value pair 

#update 
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}

d1.update(d2)
print(d1)# we print the one reiceve update

d1.update([('b', 200), ('f', 500)])
print(d1)

d1.update(b=200, d=400)