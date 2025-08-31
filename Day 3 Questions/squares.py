"""Problem 2: Print squares of numbers from 1 to n
Display the square of each number starting from 1 up to a number provided by the user.
"""

num = int(input("Enter the number:"))
for i in range(1,num + 1):
    square = i ** 2
    print("Square of ", i, "is:", square)