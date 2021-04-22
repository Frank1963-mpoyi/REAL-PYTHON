number = int(input("Enter number: ?"))
fact = 1

for num in range(1 , number+1):
    fact = fact * num
    print(f"factorial of {num} {fact}")
    
    