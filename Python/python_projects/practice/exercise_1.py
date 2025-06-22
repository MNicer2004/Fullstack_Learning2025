'''
🧠 Problem 1: Even or Odd Checker
Description:
Write a Python program that:

Asks the user to enter a number.

Checks whether the number is even or odd.

Prints a message saying whether it's even or odd.
'''
'''
user = int(input("Enter a number from 1 to 10: "))

if user in (2, 4, 6, 8, 10):       # Checks if user is one of these even numbers
    print("Even")
elif user in (1, 3, 5, 7, 9):     # Checks if user is one of these odd numbers
    print("Odd")
else:                             # If user is not in 1–10
    print("Enter a number from 1-10 only.")
''' '''
#much better way
user = int(input("Enter a number: "))

if user % 2 == 0:
    print("Even")
else:
    print("Odd")
'''
'''
🧩 Problem 2: Number Range Checker
Ask the user to enter a number.

If the number is less than 1, print "Too low!"

If the number is greater than 10, print "Too high!"

If the number is between 1 and 10, print "Just right!"
'''
'''
number = (int(input("Please enter a number: ")))

if (number < 1):
    print("Too Low!")
elif (number > 10):
    print("Too High!")
elif (number >=1 and number <=10):
    print("Just right!")          
'''
'''
🧩 Problem: Grade Checker
Ask the user to enter a test score (from 0 to 100).

Then print the grade:

90 to 100 → "Grade: A"

80 to 89 → "Grade: B"

70 to 79 → "Grade: C"

60 to 69 → "Grade: D"

0 to 59 → "Grade: F"

If the number is not between 0 and 100, print "Invalid score."
'''
'''
userName = input("Name: ")
userInput = input("Enter your test score: ")

if not userInput.isdigit():
    print("Only numbers are allowed.")
else:
    userScore = int(userInput)

    if 0 <= userScore <= 59:
        print(f"{userName}, Grade: F")
    elif 60 <= userScore <= 69:
        print(f"{userName}, Grade: D")
    elif 70 <= userScore <= 79:
        print(f"{userName}, Grade: C")
    elif 80 <= userScore <= 89:
        print(f"{userName}, Grade: B")
    elif 90 <= userScore <= 100:
        print(f"{userName}, Grade: A")
    else:
        print("The test score must be between 0 and 100.")
'''


# username = (input("Username: "))
# password = (input("Password: "))

# if username  == "Admin":            #I used nested if else here
#     if password == "admin123":
#         print("Welcome Admin!")
#     else:
#         print("Wrong password!")
# elif username and  password == 'abcdefghijklmnopqrstuvwxyz' or 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': #for this is used (and,or)
#     print("Welcome User!");
# else:
#     print("Account not found!")