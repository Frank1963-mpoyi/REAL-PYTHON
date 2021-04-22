'''
Module contents can be imported from within a function definition. In that case, 
the import does not occur until the function is called:

'''

def bar():
    # import the mod with his function foo inside another 
    # function but will not be executed until we cal this function 
    from mod import foo
    foo('corge')
    
    
bar()


# However, Python 3 does not allow the indiscriminate import * syntax from within a function:
# >>> def bar():
# ...     from mod import *
# ...
# SyntaxError: import * only allowed at module level


