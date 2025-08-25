#Code for activity suggestion on weather card
weather = input("Enter the weather condition (sunny / rainy / cloudy / snowy:)").lower()
match weather:
    case "sunny":
        print("Great day for a picnic")
    case "rainy":
        print("Stay indoor and read books")
    case "cloudy":
        print("Walkj= time")
    case "snowy":
        print("Go to mountains")
    case _:
        print("Unknown weather confition")