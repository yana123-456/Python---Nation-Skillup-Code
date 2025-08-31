"""Problem 3: Countdown timer
Implement a countdown that starts from a user-given number and decreases to 1, displaying the remaining time at each step."""

second = int(input("Enter the countdown time in seconds:"))
while second > 0:
    print("Time Left:", second)
    second -= 1