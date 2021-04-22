'''
#The else Clause
#==============
A for loop can have an else clause as well. The interpretation is analogous to that of a while loop.
The else clause will be executed if the loop terminates through exhaustion of the iterable
'''

for i in ['foo', 'bar', 'baz', 'qux']:
    print(i)
else:
    print('Done.')  # Will execute after every thing is done like close message
    

    
print("\n")    
for i in ['foo', 'bar', 'baz', 'qux']:
    if i == 'bar':
        break
    print(i)
else:
    print('Done.')  # Will not execute
