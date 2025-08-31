"""Problem 1: Print each item in a shopping list
The problem is to take shopping items as input from the user and display them one by one in a structured format."""

items = input("Enter the shopping items that have to be added in the list:").split(',')

for item in items:
    print("Buy:",item.strip())
    