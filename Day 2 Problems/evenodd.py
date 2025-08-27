"""Given a positive integer x. Your task is to check, if it is even or odd (Any number that gives zero as remainder when divided by 2 is an even number).
Note: Return "Even" if the number is even; otherwise, return "Odd"."""

def checkOddEven(x):
    if x % 2 == 0:
        return("Even")
    else:
        return("Odd")
x = int(input("Enter the number:"))
result = checkOddEven(x)
print("The number is", result)