
# if else better way
# age = 18
# message = "Adult" if age >= 18 else "Minor" if age <= 17 else "Bata kapa" if age == 10 else "Error"
# print(message)

# if else normal
# age = 21
# if age == 21:
#    print("You are 21 years old")
# elif age < 21:
#    print("You are less than 21 years old")
# for x in range(5):
#    print(x)


fullName = "Mark Christian E. Nicer"
age = 21
print(f"Hello, my name is {fullName} and I am {age} years old.")
print("Hello my name is " + fullName + " and I am " + str(age) + " years old.")
print(age)
print(fullName + " " + (str(age)))
print(f"{fullName} is so handsome and he is {age} now.")

# Input and Output
name = input("What is your name? ")
print(f"Hello, {name}!")

age = input("How old are you?")
print(f"You are {age} years old {name}!")

qualified = False
if qualified == True:
    print("You are qualified")
else:
    print("You are not qualified")


# converting text into int


money = "1000"
add = 2000
text = "hi"

print(text + " " + int(money + add))


# basic calculator

firstNumber = int(input("Enter your first number: "))
secondNumber = int(input("Enter your second number: "))

print("Do you want to add, subtract, multiply or divide? (a/s/m/d)")
choice = input("Enter your choice: ")
if choice == 'a':
    result = firstNumber + secondNumber
    print(
        f"The result of adding {firstNumber} + {secondNumber} = {result}")
elif choice == 's':
    result = firstNumber - secondNumber
    print(
        f"The result of subtracting {firstNumber} - {secondNumber} = {result}")
elif choice == 'm':
    result = firstNumber * secondNumber
    print(
        f"The result of multiplying {firstNumber} * {secondNumber} = {result}")
elif choice == 'd':
    if secondNumber != 0:
        result = firstNumber / secondNumber
        print(
            f"The result of dividing {firstNumber} / {secondNumber} = {result}")

