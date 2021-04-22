__all__ = [
        'mod1',
        'mod2',
        'mod3',
        'mod4'
        ]
#Now from pkg import * imports all four modules:
# this allow you to import all modules


'''
Hmph. Not much. You might have expected (assuming you had any expectations at all) that Python would dive down into the package directory, find all the modules it could, and import them all. But as you can see, by default that is not what happens.

Instead, Python follows this convention: if the __init__.py file in the package directory contains a list named __all__, it is taken to be a list of modules that should be imported when the statement from <package_name> import * is encountered.

For the present example, suppose you create an __init__.py in the pkg directory like this:




'''


'''
Using import * still isn’t considered terrific form, any more for packages than for modules. But this facility at least gives the creator of the package some control over what happens when import * is specified. (In fact, it provides the capability to disallow it entirely, simply by declining to define __all__ at all. As you have seen, the default behavior for packages is to import nothing.)

By the way, __all__ can be defined in a module as well and serves the same purpose: to control what is imported with import *. For example, modify mod1.py as follows:


'''