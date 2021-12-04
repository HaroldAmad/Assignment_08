import random

print("-----Number Guesser Simulator-----")

game = True
num = random.randint(0,100)

while game:
    guess = int(input("Your guess: "))
    if guess > num:
        print("Greater Than")
    elif guess < num:
        print("Less Than")
    elif guess == num:
        print("====You are Correct!!!====")
        break