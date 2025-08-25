#Code to check if a user has balance to buy an item
balance = float(input("Enter your balance:"))
price = float(input("Enter the price:"))
if balance >= price:
    print("Purchased Successful")
else:
    print("Purchased Unsuccessful")