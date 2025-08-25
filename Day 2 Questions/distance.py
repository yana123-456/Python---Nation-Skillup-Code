#Code to suggest a mode of transpirt based on distance
distance = float(input("Enter the distance:"))
if distance <=2:
    print("You can walk")
elif distance <=10:
    print("Use Bicycle and Scooter")
elif distance <=50:
    print("Use Car or Public Transport")
else:
    print("Use Train or Aeroplane")