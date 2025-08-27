"""Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.

Return True for the following cases:

Either a or b (not both) is non-negative and the flag is false.
Both a and b are negative and the flag is true."""

class Solution:
    def checkStatus(self, a,b,flag):
        if not flag and ((a >=0 and b < 0) or (a < 0 and b >=0)):
            return True
        elif flag and (a < 0 and b < 0):
            return True
        else:
            return False
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
flag_input = input("Enter the flag (True or False):").strip().lower()
flag = flag_input == "true"
sol = Solution()
result = sol.checkStatus(a,b,flag)
print("Result:", result)