import random

print("-----Number Guesser Simulator-----")

game = True
num = random.randint(0,100)

while game:
    guess = int(input("Your guess: "))