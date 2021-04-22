'''
from <module_name> import <name(s)>
An alternate form of the import statement allows individual objects from 
the module to be imported directly into the caller’s symbol table:

'''

#Syntax

# from <module_name> import <name(s)>

#Exemple
from mod import foo, s 

print(s)

# Because this form of import places the object names directly into the caller’s
# symbol table, any objects that already exist with the same name will be overwritten:


# this s will override the one imported 
s = [5, 6, 7]

print(s)



# It is even possible to indiscriminately import everything from a module at one fell swoop:

# Syntax
#from <module_name> import *

from mod import *

# Note:
'''
This isn’t necessarily recommended in large-scale production code. It’s a bit dangerous 
because you are entering names into the local symbol table en masse. Unless you know them
all well and can be confident there won’t be a conflict, you have a decent chance of 
overwriting an existing name inadvertently. However, this syntax is quite handy when 
you are just mucking around with the interactive interpreter, for testing or discovery 
purposes, because it quickly gives you access to everything a module has to offer without 
a lot of typing.

'''

#from <module_name> import <name> as <alt_name>
#from <module_name> import <name> as <alt_name>[, <name> as <alt_name> …]

# >>> s = 'foo'
# >>> a = ['foo', 'bar', 'baz']

from mod import s as string, a as alist

print(string)
print(alist)

'''
import <module_name> as <alt_name>
You can also import an entire module under an alternate name:

'''

import mod as my_module

print(my_module.s)

