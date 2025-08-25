#Code to check battery status
battery = int(input("Enter the battery percentage:"))
if battery > 80:
    print("Full Charged")
elif battery >40:
    print("Half Charged")
else:
    print("Low Battery")