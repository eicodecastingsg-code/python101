# Build a math quiz program!

import random

score = 0

while True:

    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    operator = random.randint(1, 2)


    if operator == 1:
        ActualAnswer = num1 + num2
        UserAnswer = int(input(f"What's {num1} + {num2}?: "))
    elif operator == 2:
        ActualAnswer = num1 - num2
        UserAnswer = int(input(f"What's {num1} - {num2}?: "))


    if UserAnswer == ActualAnswer:
        score = score + 1
        print("That's correct!")
    else:
        print("Wrong answer dude...")


    print(f"Your score: {score}\n")


