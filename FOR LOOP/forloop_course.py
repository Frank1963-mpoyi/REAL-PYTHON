#Numeric Range Loop
'''
The most basic for loop is a simple numeric 
range statement with start and end values.

'''

# for <var> in <iterable>: # var : any variable , iterable means an objects you want to itearate like list, tuple, string ect... or a range of numbers
#      <statement(s)> : statement you want to iterate through can be the itearble value or a name you want to count 
#Note: statement  are executed once for each item in <iterable>. 



# this type of loop they called it collection based or iterator based loop 
#because it iterate over an object example over a list , a string , tuple, etc rather than specifying numeric values or conditions:
for i in [0,1,2,3,4,5]: #for i in <collection>:
    print(i)#<loop body>
    print("\n")
# it print 1 first go up in the main print 2, go up again print 3, until it finish all the iterations  




    
#EXEMPLE 
for i in range(1,10):
    print(i, end="") # end="" mean same line
    print()# empty mean newline 
# i wil represent each value from 1 to 9 , 10is exclude from the loop


for i in range(1,10):
    print("Frank", end="")
    
# will print the word "Frank " 10 times because the range is from 1 to 10

for i in range(1, 10):
    a = 5
    b= 5
    c = a+b
    print(c)
#  will print the result 10 ten times

'''
a = ['foo', 'bar', 'baz']
for i in a:
    print(i)
...
foo
bar
baz


In this example, <iterable> is the list a, and <var> is the variable i. 
Each time through the loop, i takes on a successive item in a, so print() 
displays the values 'foo', 'bar', and 'baz', respectively. A for loop 
like this is the Pythonic way to process the items in an iterable.


'''



