#Code to login using username and password
username = input("Enter the username:")
password = input("Enter the password:")
if username == "admin":
    if password == "1234":
        print("Access Granted")
    else:
        print("Incorrect Password")
else:
    print("Username not found")
    