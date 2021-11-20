#猜数字小游戏,10次机会，猜0~20之间的一个数

import random

def guessNumber(maxCount, minNumber, maxNumber):
    number = random.randint(minNumber,maxNumber)
    
    count = 0
    while count < maxCount:
        if count == 0:
            print("Please guess a number between " + str(minNumber) + " and " + str(maxNumber) + ":")

        try:
            inputNumber = int(input())
        except ValueError:
            print("You must input a number")
            continue

        #print(type(inputNumber))
        if (inputNumber<0) or (inputNumber>20):
            print("Please input right number")
            continue
    
        count += 1
        if inputNumber == number:
            print("Good job, you guess the number in " + str(count) + " guesses!")
            break
        elif count < maxCount:
            if inputNumber > number:
                print("You guess is too high, please try again", end=", ")
            else:
                print("You guess is too low, please try again", end=", ")
            print("you have " + str(10 - count) + " chance")
            continue
        elif count == maxCount:
            print("Sorry, you lose the game")
            break
        else:
            print("Wrong game")
            break


guessNumber(5, 0, 20)