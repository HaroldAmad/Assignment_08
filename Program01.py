import random
print("========Lottery Machine========")

def lottery ():
    winningNumbers = []

    for i in range(0,3):
        number = random.randint(0,9)
        while number in winningNumbers:
            number = random.randint(0,9)

        winningNumbers.append(number)
    winningNumbers.sort
    return winningNumbers