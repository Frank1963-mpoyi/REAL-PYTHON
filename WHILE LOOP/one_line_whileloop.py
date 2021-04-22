'''
One-Line while Loops
As with an if statement, a while loop can be specified on one line. 
If there are multiple statements in the block that makes up the loop body, 
they can be separated by semicolons (;):


'''

n = 5
while n > 0: n -= 1; print(n)


# This only works with simple statements though. You can’t combine two compound statements into one line. Thus, you can specify a while 
# loop all on one line as above, and you write an if statement on one line

if True: print('foo')

# But you can not do this 

while n > 0: n -= 1; if True: print('foo') #SyntaxError: invalid syntax
