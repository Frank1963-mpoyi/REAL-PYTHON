n = 5
while n > 0:
    n -= 1
    if n == 2:# when this condition is met its jump it and continue the rest of the loop
        continue
    print(n)
print('Loop ended.')

# Note : This time, when n is 2, the continue statement causes termination of that iteration. 
# Thus, 2 isn’t printed. Execution returns to the top of the loop, the condition is re-evaluated, 
# and it is still true. The loop resumes, terminating when n becomes 0, as previously.


'''
The else Clause
Python allows an optional else clause at the end of a while loop. This is a unique 
feature of Python, not found in most other programming languages. The syntax is shown below:

while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>
    
The <additional_statement(s)> specified in the else clause will be executed when the while loop terminates.


'''
