''' Iteration means executing the same block of code over and over, potentially many times. A programming structure that implements iteration is called a loop'''

'''
In programming, there are two types of iteration, indefinite and definite:

With indefinite iteration, the number of times the loop is executed isn’t 
specified explicitly in advance. Rather, the designated block is executed 
repeatedly as long as some condition is met.

With definite iteration, the number of times the designated block will be 
executed is specified explicitly at the time the loop starts.



while <expr>:
    <statement(s)>
    
<statement(s)> represents the block to be repeatedly executed, often referred 
to as the body of the loop. This is denoted with indentation, just as in an if statement.
'''

a = 0# initialise

while a <= 5: # to check Boolean condition if its True it will execute the body
    # then when a variale will do addition it will be 0+1=1 go again to check the condition like new value
    # of a = 1 and 1<=5 True it print and add again 1+1=2 2<=5, 2+1= 3 , 3<=5, until 6<=5 no the condition become false
    # and the loop terminate
    print(a)# you can print the a value for each iteration 
    # print("Frank") or you can print Frank the number of the iterations
    a = a + 1# increment to make the initialize condition become false in order to get out of the loop
    
    
#Note : Note that the controlling expression of the while loop is tested first, 
# before anything else happens. If it’s false to start with, the loop body will never 
# be executed at all:

family = ['mpoyi', 'mitongu', 'kamuanya', 'sharon', 'ndaya', 'mbuyi', 'tshibuyi']

while family:#When a list is evaluated in Boolean context, it is truthy if it has elements in it and falsy if it is empty
    print(family.pop(-1)) # for every iteration it will remove the last element in the list until the list is finish 
#Once all the items have been removed with the .pop() method and the list is empty, a is false, and the loop terminates.    

