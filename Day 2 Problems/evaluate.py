"""Evaluate Formulae
Given four inputs that are stored in variables a, b, c, and d. You need to write an expression to evaluate the following formula. Use integer division. The expression should be a single statement.
Print ((a + b) // c) + d"""

class Solution:
    def calculate(self, a: int, b: int, c: int, d: int) -> int:
        #Code here
        return((a + b)// c) + d 
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
d = int(input("Enter the fourt number:"))
sol = Solution()
result = sol.calculate(a,b,c,d)
print("Result:",result)
