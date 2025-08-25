#Code to check mobile notification settings based on a user profile mode
mode = input("Enter the phone mode(silent / vibrate / loud / donot disturb:)").lower()
match mode:
    case "silent":
        print("Notification is muted")
    case "vibrate":
        print("Phoen will vibrate")
    case "loud":
        print("Notifications will be loud")
    case "donot disturb":
        print("No calls or notifications")
    case _:
        print("Invalid mode selected")