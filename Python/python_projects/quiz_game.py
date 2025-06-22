print("Welcome to the Python Quiz!")
username = (input("Full name: "))
block = (input("BSIT Block: "))
print(f"""
{username}, Block: {block}
Q1: What does CPU stand for?
A. Central Process Unit
B. Central Processing Unit
C. Computer Personal Unit
D. Central Performance Unit
""")
userScore = 0
answer_q1 = input("A,B,C or D? :")
question1_answer = 'B'
if answer_q1 == question1_answer:
    print("Correct!")
    userScore += 1
else:
    print("Incorrect!")

print(f"""
Q2: Which language is used to style websites?
A. HTML
B. CSS
C. Python
D. Java
""")
answer_q2 = (input("A,B,C or D? : "))
question2_answer = 'B'
if answer_q2 == question2_answer:
    print("Correct!")
    userScore +=1
else:
    print("Incorrect!")
print(f"Your final score: {userScore}/2")

if userScore == 2:
    print("Perfect Score!")
elif userScore < 2:
    print("Good Work!")
elif userScore < 1:
    print("You Failed! Better Luck Next Time.")

    
