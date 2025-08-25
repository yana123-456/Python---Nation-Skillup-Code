#Code to check if a student is pass or fail in the examination.This program determines whether a student has passed an exam. It takes the student's marks as input and uses an if-else statement to check if the marks are 40 or above, which is considered the passing score.
marks = int(input("Enter the marks:"))
if marks >= 40:
    print("You passed the exam")
else:
    print("You failed the exam")