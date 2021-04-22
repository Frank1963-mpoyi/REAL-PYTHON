
# About now, you may be thinking, “How is that useful?” You could accomplish the same thing by 
# putting those statements immediately after the while loop, without the else:

#Example 

b = 0
while b<5:
    b +=1
    print(b)
print("The loop is terminated")


b = 0
while b<5:
    b +=1
    print(b)
else:
    print("The loop is terminated")

# the difference between Two is if the while loop break the else statement will not be executed 
# but with no else the print out of the loop will be print no matter  break or not

#This loop is terminated prematurely with break, so the else clause isn’t executed.


a = ['foo', 'bar', 'baz', 'qux']
s = 'corge'

i = 0
while i < len(a):
    if a[i] == s:#a[0] beacuse i value is 0
        # Processing for item found
        break
    i += 1
else:
    # Processing for item not found
    print(s, 'not found in list.')


'''
Note: The code shown above is useful to illustrate the concept, but you’d actually be very unlikely to search a list that way.

First of all, lists are usually processed with definite iteration, not a while loop. Definite iteration is covered in the next tutorial in this series.

Secondly, Python provides built-in ways to search for an item in a list. You can use the in operator:

if s in a:
...     print(s, 'found in list.')
... else:
...     print(s, 'not found in list.')
...
corge not found in list


The list.index() method would also work. This method raises a ValueError exception if the item isn’t found in the list, so you need to understand exception handling to use it. In Python, you use a try statement to handle an exception. An example is given below:
>>> try:
...     print(a.index('corge'))
... except ValueError:
...     print(s, 'not found in list.')
...
corge not found in list.

'''
