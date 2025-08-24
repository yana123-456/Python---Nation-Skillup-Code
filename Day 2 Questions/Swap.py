#Swap two numbers using operators only.
#1. Using Arithmetic Operators
a,b = 5,10
a = a + b
b = a - b
a = a - b
b = a - b
print(a,b)

#2. Using XOR Operators
a,b = 5,10
a = a ^ b
b = a ^ b
a = a ^ b
print(a,b)
