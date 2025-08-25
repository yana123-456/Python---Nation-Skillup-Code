"""Logical operators and, or, not are used in condition checking. Like a and b checks if both a and b are True. First a is checked then b is checked. a or b checks if either of a or b is True. If one is True; it doesn't check for the other. not a complements the boolean value of a.
Note: 0 and empty string are False and all other values are True.
In this question you basically need to do
a and b
a or b
not a

"""
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
p = a and b
q = a or b
r = not a 
print(p,q,r)