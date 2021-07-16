""" Passing Multiple Arguments to a Function    """

#*args and **kwargs  allow to pass many keyword argument  and many argument to the function 

def my_sum(a, b):
    return a + b
# this function work fine but it only limited by two argument 



def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result

list_of_integers = [1, 2, 3]
print(my_sum(list_of_integers))

# this pratic is good but you must always pass the list to the function when you are calling it 
# but you will never know the length of the list 


# this is the *args is very helpfull bcz it help you to pass a varying list of argument
# sum_integers_args.py

def my_sum(*args): #unpacking operator (*) is import name doesnt matter
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3)) # here no need to pass a list you just pass position argument


# (*args) this iterable object is not a list is a tuple 
#  A tuple is similar to a list in that they both support slicing and iteration.





