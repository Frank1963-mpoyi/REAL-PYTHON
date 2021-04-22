

# BREAK 
#======

n = 5
while n > 0:
    n -= 1
    if n == 2: # if this condition is True it will break the loop not continue is not going to execute it
        # even the rest of the body will be stoped
        break
    print(n)
print('Loop ended.')

#When n becomes 2, the break statement is executed. The loop is terminated completely, and program execution jumps to the print() statement on line 7.


family = ['mpoyi', 'mitongu', 'kamuanya', 'sharon', 'ndaya', 'mbuyi', 'tshibuyi']

while family:
    print(family[5].pop(-1))
    break
