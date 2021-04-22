'''
Altering for Loop Behavior
You saw in the previous tutorial in this introductory series how execution of a while loop can be interrupted with break and continue statements and modified with an else clause. These capabilities are available with the for loop as well.

The break and continue Statements
break and continue work the same way with for loops as with while loops. break terminates the loop completely and proceeds to the first statement following the loop:



'''
# BREAK
#=======
for i in ['mpoyi', 'mitongu', 'children', 'others', 'people','all_together']:
    if 'others'  in i :
        break
    print(i)
    
#break terminates the loop completely dont even mentions the other left after mathiew



# CONTINUE
#==========
print("\n")
for i in ['kanana', 'mukuna', 'kayowa', 'mutombo', 'mathiew']:
    if 'mathiew'  in i :
        continue
    print(i)
# just ignore mention and continue to print the rest of the loop 


# PASS
#======
print("\n")
for i in ['kanana', 'mukuna', 'kayowa', 'mutombo', 'mathiew']:
    if 'mathiew'  in i :
        pass
    print(i)
# pass means dont give an error just pass 