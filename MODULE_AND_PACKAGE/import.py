import mod


print("\n")
# access string
print(mod.s)

# access list
print(mod.a)

print()
# acess function
mod.foo(['quux', 'corge', 'grault'])

#access class
x = mod.Foo()
print(x)






# import mod
#When the interpreter executes the above import statement, 
# it searches for mod.py in a list of directories assembled 
# from the following sources:

# 1. The directory from which the input script was run or the current 
# directory if the interpreter is being run interactively

# 2. The list of directories contained in the PYTHONPATH environment 
# variable, if it is set. (The format for PYTHONPATH is OS-dependent 
# but should mimic the PATH environment variable.)

# 3. An installation-dependent list of directories configured at the 
# time Python is installed

#The resulting search path is accessible in the Python variable sys.path, which is obtained from a module named sys:

print("\n")
import sys

print(sys.path)

print("\n")





# IMPORT OUTSIDE PYTHON PATH DIRECTORIES
#=======================================

# here is to import the file outside of the python path directory 
sys.path.append(r'C:\Users\MPOYI TSHIBUYI\Documents')
#sys.path

import working_hours

#print(working_hours.__file__)
#working_hours.<fuction_string_class_ect....>

# From the caller, objects in the module are only accessible 
# when prefixed with <module_name> via dot notation, as illustrated below.

# import <module_name>
# The simplest form is the one already shown above:

'''
From the caller, objects in the module are only accessible when prefixed with <module_name> via dot notation, as illustrated below.

After the following import statement, mod is placed into the local symbol table. Thus, mod has meaning in the caller’s local context:

import mod
mod


But s and foo remain in the module’s private symbol table and are not meaningful in the local context:
>>> s
NameError: name 's' is not defined
>>> foo('quux')
NameError: name 'foo' is not defined

To be accessed in the local context, names of objects defined in the module must be prefixed by mod:
>>> mod.s
'If Comrade Napoleon says it, it must be right.'
>>> mod.foo('quux')
arg = quux


Several comma-separated modules may be specified in a single import statement
import <module_name>[, <module_name> ...]
'''
# EXEMPLE 

