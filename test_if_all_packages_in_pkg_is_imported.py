from MODULE_AND_PACKAGE.pkg import * 



# this is to test if all module are imported to import them you must put them 
# in __init__.py 
print(dir())

# its good instead of importing one by one 
# from MODULE_AND_PACKAGE.pkg import mod1
# from MODULE_AND_PACKAGE.pkg import mod2
# from MODULE_AND_PACKAGE.pkg import mod3
# from MODULE_AND_PACKAGE.pkg import mod4


# print(dir()) # is to check if all are imported 
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', 
# '__loader__', '__name__', '__package__', 
# '__spec__', 'mod1', 'mod2', 'mod3', 'mod4']

from MODULE_AND_PACKAGE.main_package.sub_package1 import mod2

print(mod2.a)

