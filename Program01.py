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

def guess ():
    userGuess = []

    for i in range (0,3):
        hula = int(input("Enter Your number between 0 and 9: "))
        while (hula in userGuess or hula<0 or hula>9):
                print("Invalid guess, try again")
                hula = int(input("Enter Your number between 0 and 9: "))
    
        userGuess.append(hula)
    userGuess.sort
    return userGuess

winningFunc = lottery()
userFunc = guess()
