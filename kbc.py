"""In KBC the player is presented with 1 question and 4 options, where 1 option is correct
user chooses the right option they get a reward and move to next question 
if they give wrong ans the game ends"""


playerName = str(input("Enter your Name:"))
print(f"Welcome to Kaun Banega Crorepati, {playerName}\n")

print('''Game Rules:

Question Progression: Players are presented with one question at a time. Each correct answer advances the player to the next round with a more challenging question.\n
Multiple Choice: Every question comes with four possible answers (A, B, C, D). Only one is correct.\n
Lifeline: Players have access to one lifeline called "50-50". When used, two incorrect options are removed, leaving the correct answer and one wrong option.\n
Game Over: If a player answers incorrectly at any point, the game ends immediately.\n
Winning: The ultimate goal is to answer all questions correctly and reach the final round.\n''')


playerstart = input("Ready to get started Press Y/N: \n ").upper()

if playerstart == "Y":
    print(f"{playerName}, Let,s start Kaun Banega Crorepati.\n Your first question!\n")
elif playerstart == "N":
    print(f"{playerName}, Bye Take care")
    exit

question = [
    ["what is the capital of India?", ["A - Delhi", "B - Kanpur", "C - Mumbai", "D - Goa"], "A"],
 ["which is a primary colour?",["A - Black", "B - Grey", "C - Violet", "D - Red"], "D"],
    ["Which planet is known as the Red planet?", ["A- Venus", "B- Earth", "C - Mars", "D - Saturn"], "C"],
]


def useranswer():
    for q in question:
        global questions 
        questions = q[0]
        global options
        options = q[1]
        answer = q[2]

        print(questions)
        for x in options:
            print(x)
        
        global userinput
        userinput = input("enter your answer").upper().strip()

        if userinput == "L":
            lifeline(userinput)

        if userinput == answer:
            print(f"{answer}, is the correct answer")
        
        
        else:
            print("better luck next time")
            print()
            exit()

useranswer()
