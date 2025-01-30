import random
import os

def clearConsole():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Mac/Linux
        os.system('clear')

def RPS():
    clearConsole()
    import random

    # AI choice
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

    # Get user input and convert to an integer
    userChoice = input("1, 2 or 3: ")

    # Ensure userChoice is an integer
    if userChoice not in ["1", "2", "3"]:
        print("Invalid choice. Please enter 1, 2, or 3.")
    else:
        userChoice = int(userChoice)  # Convert input to integer

        print(f"AI chose: {aiChoiceText}")

        # Determine winner
        if userChoice == aiChoice:
            print("You tied")
        elif (userChoice == 1 and aiChoice == 2) or (userChoice == 2 and aiChoice == 3) or (
                userChoice == 3 and aiChoice == 1):
            print("You lose!")
        else:
            print("You win!")

    print("\nPress enter to play again!")
    print("Press CTRL+C to exit")
    input()
    RPS()

RPS()
