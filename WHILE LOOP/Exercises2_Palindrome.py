number = int(input("Enter any number : ? "))
cpy = number
rev = 0

while number != 0:
    r = number % 10
    rev = rev * 10 + r
    number = int(number/10)
    if cpy == rev:
        print("Given number is polindrome")
    else:
        print("Not polindrome")
        
        
# 1551