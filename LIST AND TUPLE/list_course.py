'''
Lists and tuples are arguably Python’s most versatile, useful data types. 
You will find them in virtually every nontrivial Python program.


Python Lists
=============

In short, a list is a collection of arbitrary objects, somewhat akin to an 
array in many other programming languages but more flexible. Lists are defined 
in Python by enclosing a comma-separated sequence of objects in square brackets 
([]), as shown below


a = ['foo', 'bar', 'baz', 'qux']



The important characteristics of Python lists are as follows:

Lists are ordered.
Lists can contain any arbitrary objects.
List elements can be accessed by index.
Lists can be nested to arbitrary depth.
Lists are mutable.
Lists are dynamic.

'''

#Lists that have the same elements in a different order are not the same:

# EXEMPLE 
a = ['foo', 'bar', 'baz', 'qux']
b = ['baz', 'qux', 'bar', 'foo']

a == b # false are not the same even if they have the same element in different order


[1, 2, 3, 4] == [4, 1, 3, 2] # false not the same

# Lists Can Contain Arbitrary Objects
#=======    ==============    ========

# A list can contain any assortment of objects. The elements of a list can all be the same 
# type:

a = [2, 4, 6, 8]

#Or the elements can be of varying types:
a = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]

#A list can contain any number of objects, from zero to as many as your computer’s memory will allow:
a = []
print(a)

a = [ 'foo' ]


#List objects needn’t be unique. A given object can appear in a list multiple times
a = ['bark', 'meow', 'woof', 'bark', 'cheep', 'bark']

'''
List Elements Can Be Accessed by Index
Individual elements in a list can be accessed using an index in square brackets. 
This is exactly analogous to accessing individual characters in a string. 
List indexing is zero-based as it is with strings.


'''


a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[0])

print(a[-1])

#Slicing also works. If a is a list, the expression a[m:n] 
# returns the portion of a from index m to, but not including, index n:

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print( a[2:5])