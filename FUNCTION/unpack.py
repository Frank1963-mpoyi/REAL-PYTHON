"""   Unpacking With the Asterisk Operators: * & **  """

#the unpacking operators are operators 
# that unpack the values from iterable objects in Python (iterable are list, tuple, dictionary )

# * can be use of list, tuple, set
# ** can be use for dictionary 

my_list = [1, 2, 3]
print(my_list)

print(*my_list)# this method print one by one 


# unpacking_call.py
def my_sum(a, b, c):
    print(a + b + c)

my_list = [1, 2, 3]
my_sum(*my_list)

#Here, my_sum() explicitly states that a, b, and c are required arguments.



# sum_integers_args_3.py
def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]

print(my_sum(*list1, *list2, *list3))

# when you unpack list1, list2, list3 it act like you pass soingle element alone
print(my_sum(1,2,3,4,5,6,7,8,9)) # same as this 


my_list = [1, 2, 3, 4, 5, 6]
a, *b, c = my_list

print(a)
print(b)
print(c)

# merging_lists.py
my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]


# merging_dicts.py
my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}

print(my_merged_dict)

# it can unpack string
a = [*"RealPython"]
print(a)

'''

Iterable is an object, which one can iterate over. It generates an Iterator when passed to iter() method. Iterator is an object, which is used to iterate over an iterable object using __next__() method. ... Note that every iterator is also an iterable, but not every iterable is an iterator.23 Aug. 2019


An iterable is any Python object capable of returning its members one at a time, permitting it to be iterated over in a for-loop. Familiar examples of iterables include lists, tuples, and strings - any such sequence can be iterated over in a for-loop.
'''