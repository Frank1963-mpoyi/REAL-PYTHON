'''
ITERABLES OBJECTS
====================


print(iter('foobar'))

If an object is iterable, it can be passed to the built-in Python 
function iter(), which returns something called an iterator.

>> iter('foobar')                             # String
<str_iterator object at 0x036E2750>

>>> iter(['foo', 'bar', 'baz'])                # List
<list_iterator object at 0x036E27D0>

>>> iter(('foo', 'bar', 'baz'))                # Tuple
<tuple_iterator object at 0x036E27F0>

>>> iter({'foo', 'bar', 'baz'})                # Set
<set_iterator object at 0x036DEA08>

>>> iter({'foo': 1, 'bar': 2, 'baz': 3})       # Dict
<dict_keyiterator object at 0x036DD990>
'''

'''
NO ITERABLES OBJECTS
====================


>>> iter(42)                                   # Integer
Traceback (most recent call last):
    File "<pyshell#26>", line 1, in <module>
    iter(42)
TypeError: 'int' object is not iterable

>>> iter(3.1)                                  # Float
Traceback (most recent call last):
    File "<pyshell#27>", line 1, in <module>
    iter(3.1)
TypeError: 'float' object is not iterable

>>> iter(len)                                  # Built-in function
Traceback (most recent call last):
    File "<pyshell#28>", line 1, in <module>
    iter(len)
TypeError: 'builtin_function_or_method' object is not iterable


'''
# But these are by no means the only types that you can iterate over. Many objects that are built into Python or defined in modules are designed to be iterable. For example, open files in Python are iterable. As you will see soon in the tutorial on file I/O, iterating over an open file object reads data from the file.

# In fact, almost any object in Python can be made iterable. Even user-defined objects can be designed in such a way that they can be iterated over. (You will find out how that is done in the upcoming article on object-oriented programming.)


a = ['foo', 'bar', 'baz']
itr = iter(a)
print(itr)
print(next(itr)) # The built-in function next() is used to obtain the 
#next value from in iterator.
print(next(itr))
print(next(itr))


print("\n")
family = ['Mpoyi', 'Mitongu', 'Kamuanya', 'Sharon', 'Ndaya', 'Mbuyi', 'Tshibuyi']
itr_family = iter(family)
print(list(itr_family)) # this will print all the list no need of next

itr_family = tuple(family)
print(tuple(itr_family))

itr_family = set(family)
print(set(itr_family))


# Similarly, the built-in tuple() and set() functions return a tuple and a set, 
# respectively, from all the values an iterator yields:
