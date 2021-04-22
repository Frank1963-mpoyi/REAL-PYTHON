no = int(input("Enter any number: ?"))
cpy = no 
sum = 0

while no != 0:
    r = no % 10
    sum = sum+(r*r*r)
    no = int(no/10)
    if cpy == sum:
        print("Given number is Armstrong")
    else:
        print("Not Amstrong")
        
# input 153

#Explain

'''
1 st iteration

153 != 0 True:
r = 153 % 10 #(r=3)
sum = sum+(r+r+r) #(sum = 27) 0+(3*3*3)
no = int(153/10) # its 15 because they say int only not float
if cpy == sum: # 153 not equal to 27

it will execute else part


2 nd iteration

15 ! = 0 True:
r = 15 % 10 # 5
sum = 27+(5*5*5) # 152
no = int(15/10) # 1

if 15 == 152 : # no 
else will be execute


3 rd iteration 

1 !=0 True:
r = 1 % 10 # 0
sum = 152 + (0*0*0) # 152
no = int(1/10) # 0

if 0 == 0 yes 
the 


'''


