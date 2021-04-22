# NESTED WHILE LOOP 


#In general, Python control structures can be nested within one another. 
# For example, if/elif/else conditional statements can be nested:

#EXEMPLE

gender = ["F"]
age = 0

if age < 18:
    if gender == 'M':
        print('son')
    else:
        print('daughter')
elif age >= 18 and age < 65:
    if gender == 'M':
        print('father')
    else:
        print('mother')
else:
    if gender == 'M':
        print('grandfather')
    else:
        print('grandmother')
        
#Similarly, a while loop can be contained within another while loop, as shown here:

a = ['foo', 'bar']
while len(a):
    print(a.pop(0))
    b = ['baz', 'qux']
    while len(b):
        print('>', b.pop(0))
        
        
#A break or continue statement found within nested loops applies to the nearest enclosing loop:
'''
while <expr1>:
    statement
    statement

    while <expr2>:
        statement
        statement
        break  # Applies to while <expr2>: loop

    break  # Applies to while <expr1>: loop



'''

#Additionally, while loops can be nested inside if/elif/else statements, and vice versa

'''
if <expr>:
    statement
    while <expr>:
        statement
        statement
else:
    while <expr>:
        statement
        statement
    statement



while <expr>:
    if <expr>:
        statement
    elif <expr>:
        statement
    else:
        statement

    if <expr>:
        statement
        
        
        
In fact, all the Python control structures can be intermingled with one another to whatever extent you need. That is as it should be. Imagine how frustrating it would be if there were unexpected restrictions like “A while loop can’t be contained within an if statement” or “while loops can only be nested inside one another at most four deep.” You’d have a very difficult time remembering them all.
        
'''

