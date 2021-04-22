no_patterns= int(input("Please Enter the Number of patterns: ? "))

'''
for num in range(1,no_patterns+1):
    print()
    for pict in range(1, 10):
        print(pict, end="")
    print()
    print(f"Number of iteration : {num}")# will print the number of user input for each iteration
'''

for row in range(1, no_patterns):
    for columns in range(0, row+1):
        print("*", end="")
    # print(row)
    print()