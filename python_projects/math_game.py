print("Simple Math Game!")

correctAnswer_One = 2025
correctAnswer_Two = 28
lives = 3

while lives > 0:
    try:
        questionOne = int(input("What is 300 + 1725? "))
        if questionOne == correctAnswer_One:
            print("That's Correct!")
            while True:
                questionTwo = int(input("What is 20 + 8? "))
                if questionTwo == correctAnswer_Two:
                    print("Good Job! Perfect Score.")
                    break
                else:
                    print("Try Again!")
                    lives -= 1
            if lives == 0:
                break  # Exit the outer loop if out of lives
            break  # Exit the outer loop after both questions are correct
        else:
            print("Try Again!")
            lives -= 1
    except ValueError:
        print("Please enter valid numbers.")
        continue
else:
    print("GG! Nice Try.")
        