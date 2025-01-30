import os
import random


def clearConsole():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Mac/Linux
        os.system('clear')

clearConsole()
print("The AI will pick rock paper or scissors. \nYou need to pick a choice with 1,2 or 3, and the game will run.\nPress enter.")
input()

def RPS():
    clearConsole()
    choices = ['rock', 'paper', 'scissors']

    rules = {
        'rock': ['scissors'],
        'paper': ['rock'],
        'scissors': ['paper']
    }

    aiChoice = random.choice(choices)

    print("1. Rock")
    print("2. Paper")
    print("3. Scissors \n")

    print("1, 2 or 3:")

    try:
        userInput = int(input(">>"))
    except:
        print("INCORRECT INPUT")
        return


    if userInput >= 1 or userInput <= 3:
        userChoice = choices[userInput - 1]
    else:
        print("ERROR: INVALID INPUT")
        return

    if userChoice == aiChoice:
        result = 'You both picked ' + aiChoice + '!'

    elif aiChoice in rules[userChoice]:
        result = 'You win! (' + userChoice + ' beats ' + aiChoice + ')'

    else:
        result = 'You lose! (' + userChoice + ' beats ' + aiChoice + ')'

    print(result)

    print("\nPress enter to play again!")
    print("Press CTRL+C to exit")
    input(">")
    RPS()

RPS()
