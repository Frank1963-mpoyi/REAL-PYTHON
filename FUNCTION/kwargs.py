# **kwargs is the same as *args but instead of accepting positional argument 
# kwargs accept keyword arguments

def concatenate(**kwargs): #  unpacking operator (**) you can use any name 
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result

a = concatenate(a="Real", b="Python", c="Is", d="Great", e="!")
print(a)
# NOTE: if you iterate a dictionary and want to retgurn a value you can use values() method

print("\n")
def concatenate_(**kwargs):
    result = ""
    # Iterating over the keys of the Python kwargs dictionary
    for arg in kwargs:
        result += arg
    return result

print(concatenate_(a="Real", b="Python", c="Is", d="Great", e="!"))
# this method if you dont put value you will iterate the key 


""" Ordering Arguments in a Function """

# correct_function_definition.py
def my_function(a, b, *args, **kwargs): # always follow this order
    pass