'''
The dir() Function
The built-in function dir() returns a list of defined names in a namespace. 
Without arguments, it produces an alphabetically sorted list of names in the 
current local symbol table:


'''
print(dir())

a = "yrs"
qux = [1, 2, 3, 4, 5]
print(dir())# return the list of the name of all the variable 


class Bar():
    pass

x = Bar()
print(dir())
