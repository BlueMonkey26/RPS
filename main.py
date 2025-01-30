import random
import os

def clearConsole():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Mac/Linux
        os.system('clear')

def RPS():
    clearConsole()
    aiChoice = random.randint(1, 3)

    if aiChoice == 1:
        aiChoiceText = "Rock"
    elif aiChoice == 2:
        aiChoiceText = "Paper"
    elif aiChoice == 3:
        aiChoiceText = "Scissors"

    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    userChoice = int(input("1, 2 or 3:"))

    if userChoice == aiChoice:
        print("You tied")

    elif userChoice == 1 and aiChoice == 2:
        print(aiChoiceText + "\n")
        print("You loose!")
    elif userChoice == 1 and aiChoice == 3:
        print(aiChoiceText + "\n")
        print("You win!")

    elif userChoice == 2 and aiChoice == 1:
        print(aiChoiceText + "\n")
        print("You win!")
    elif userChoice == 2 and aiChoice == 3:
        print(aiChoiceText + "\n")
        print("You loose!")

    elif userChoice == 3 and aiChoice == 1:
        print(aiChoiceText + "\n")
        print("You loose!")
    elif userChoice == 3 and aiChoice == 2:
        print(aiChoiceText + "\n")
        print("You win!")



    print("\nPress enter to play again!")
    print("Press CTRL+C to exit")
    input()
    RPS()

RPS()
