
#Iterating Through a Dictionary
#===============================

my_family = {
    'papa': 'Mpoyi', 
    'maman': "Mitongu", 
    'enfatns': 5
    }

for name in my_family:
    print(name)
    
#As you can see, when a for loop iterates through a dictionary, the loop variable is assigned to the dictionary’s keys.

print("\n")
for name in my_family:
    print(my_family[name])
    
#To access the dictionary values within the loop, you can make a dictionary reference using the key as usual


print("\n")
for v in my_family.values():
    print(f" use value function to print values : {v} ")
    
    
print("\n")

'''
In fact, you can iterate through both the keys and values of a dictionary simultaneously. 
That is because the loop variable of a for loop isn’t limited to just a single variable. 
It can also be a tuple, in which case the assignments are made from the items in the iterable 
using packing and unpacking, just as with an assignment statement:

'''
ruth, mpoyi = ('PAPA BUDILELU', 'PAPA AUGUY') # you can not unpack more than one values
#print(ruth)
print(ruth, mpoyi)


for i, j in [(1, 2), (3, 4), (5, 6)]:
    print(i, j)
    # note the value of i is the first in tuple and the value of j is the seconde in tuple 
    
    
#Note : the dictionary method .items() effectively returns a list of key/value pairs as tuples:

d = {'laptop': "Blue", 'BMW': "White", 'Bike': "green"}

print( d.items())# returns a list of key/value pairs as tuples:

#the Pythonic way to iterate through a dictionary accessing both the keys and values looks like this:

print("\n")
d = {'laptop': "Blue", 'BMW': "White", 'Bike': "green"}
# iterate key and values
for k, v in d.items():
    print(f'key= {k}  value={v}')
    print()
    