""" built-in and user-defined functions."""

""" 1. build in """

# id() , len(), print(),  any()
s = 'foobar'
check_id = id(s)
print(check_id)

any([False, False, False])
False
any([False, True, False])
True

any(['bar' == 'baz', len('foo') == 4, 'qux' in {'foo', 'bar', 'baz'}])
False

any(['bar' == 'baz', len('foo') == 3, 'qux' in {'foo', 'bar', 'baz'}])
True

# return True if any of the value in the list is True

# each of the built in function perform a task the code they are is somewhere you dont need to worries about that 

# when you make your own function it will work the same as build in function 
# the program that execute the function goes to the body of the function 
# the function is finish the  execution returns to your code where it left off
#  you’ll call your Python function and program execution will transfer to the body of code that makes up the function.

