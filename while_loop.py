'''
if you want to repeat a statement like print("Mpoyi) 100 times you can copy and paste 100
times but its a hard work and it will also take too much space

'''

i = 1
while i <= 5:
    print("Hello Mpoyi")
    i=i+1
    

print('\n')

'''
i = 1
while i <= 5:
    print("Hello Mpoyi", i)
    i=i+1
'''

#====== NESTED WHILE LOOP
i = 5
while i>=1:
    print("Frank ", end="")
    
    j=1
    while j<=4:
        print("Mpoyi ", end="")
        j= j+1
    i = i - 1
    print()# come in the new line
    
    
'''
Nested the main while print "Frank" and go to Nested Loop
it will execute nested loop until the condition is false

and go back again to main loop print "Frank" and go to Nested Loop 
it will execute nested loop until the condition of nested loop is false and jump again to main loop until main loop condition is finish


the principe is like 1 days 24hrs like monday run 24hrs when it finish tuesday run 24hrs when it finish wesday run 24hrs ect...
'''

#Note : end="" means stay on the same line 

