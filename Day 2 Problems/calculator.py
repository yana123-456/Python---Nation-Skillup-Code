"""Given two numbers a and b; you need to perform basic mathematical operation on them. You will be provided an integer named as operator. 
If operator equals to 1 add a and b, then print the result as a string.
If operator equals to 2 subtract b from a, then print the result as a string.
If operator equals to 3 multiply a and b, then print the result as a string.
If operator equals to any another number, print "Invalid Input"(without quotes).
Note: Do not add a new line at the end"""

def utility(a, b, opr):
    if opr == 1:
        print(str(a +b), end = "")
    elif opr == 2:
        print(str(a - b), end="")
    elif opr == 3:
        print(str(a * b), end ="")
    else: 
        print("Invalid operators", end="")
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
opr = int(input("Enter 1 for + , Enter 2 for - , Enter 3 for *:"))
utility(a,b,opr)   