#Infinite Loops
#===============
# Suppose you write a while loop that theoretically never ends. Sounds weird, right?

while True:
    print('foo')
    
    
# This code was terminated by Ctrl+C, which generates an interrupt from the keyboard.
# Otherwise, it would have gone on unendingly. 

'''
More prosaically, remember that loops can be broken out of with the break statement. It may be more straightforward to terminate a loop based on conditions recognized within the loop body, 
rather than on a condition evaluated at the top.


Here’s another variant of the loop shown above that successively removes items from a list using .pop() until it is empty:
>>> a = ['foo', 'bar', 'baz']
>>> while True:
...     if not a:
...         break
...     print(a.pop(-1))
...
baz
bar
foo
'''