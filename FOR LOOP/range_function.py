#The range() Function
'''
a numeric range loop, in which starting and ending numeric values are specified. Although this form of for loop isn’t directly built into Python, it is easily arrived at.

For example, if you wanted to iterate through the values from 0 to 4, you could simply do this:

'''

for n in (0, 1, 2, 3, 4):
    print(n)
    
# This solution isn’t too bad when there are just a few numbers. 
# But if the number range were much larger, it would become tedious
# pretty quickly.

'''
Happily, Python provides a better option—the built-in range() function,
which returns an iterable that yields a sequence of integers.

range(<end>) returns an iterable that yields integers starting with 0,
up to but not including <end>:


'''
print()

x = range(5)
print(x)
print(type(x))

print(range(0, 15))

# Note that range() returns an object of class range, not a list or tuple of the values. Because a range object is an iterable, you can obtain the values by iterating over them with a for loop:

x = range(5)
list(x)
tuple(x)
print(list(x))
print(tuple(x))
for n in x:
    print(n)
    
# However, when range() is used in code that is part of a larger application, 
# it is typically considered poor practice to use list() or tuple() in this way. 
# Like iterators, range objects are lazy—the values in the specified range are not 
# generated until they are requested. Using list() or tuple() on a range object forces
# all the values to be returned at once. This is rarely necessary, and if the list is long,
# it can waste time and memory.


print(list(range(5, 20, 3)))
#range(<begin>, <end>, <stride>) returns an iterable that yields integers starting with 
# <begin>, up to but not including <end>. If specified, <stride> indicates an amount to skip 
# between values (analogous to the stride value used for string and list slicing):

#If <stride> is omitted, it defaults to 1:
print( list(range(5, 10, 1)))
print( list(range(5, 10)))# if stride is omiited the default is one 

print(list(range(-5, 5))) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

print(list(range(5, -5)))#[]

print(list(range(5, -5, -1)))# [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]