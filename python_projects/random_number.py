import random

randomOne = random.randint(1, 6)
randomTwo = random.randint(1, 4)
print("GUESS THE NUMBER!")
while True:
    try:
        guessOne = int(input("Guess the first number (1-6): "))
        guessTwo = int(input("Guess the second number (1-4): "))
        
    except ValueError:
        print("Please enter valid numbers.")
        continue

    if guessOne == randomOne and guessTwo == randomTwo:
        print("Congratulations! You guessed both numbers correctly.")
        break
    else:
        print("Incorrect guess. Try again.")

    