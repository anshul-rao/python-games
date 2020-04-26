# Rock Paper Scissors
# Made by TheQuantumRobot

# -------------------------

import random

# ------- Functions -------


def startGame():
    while True:
        rpsOptions = ["Rock", "Paper", "Scissors"]

        playerChoice = input("\nChoose Rock, Paper or Scissors: ").lower()
        while (
            playerChoice != "rock"
            and playerChoice != "paper"
            and playerChoice != "scissors"
        ):
            playerChoice = input("\nChoose Rock, Paper or Scissors: ").lower()

        computerChoice = (random.choice(rpsOptions)).lower()

        print(
            "You have chosen "
            + playerChoice
            + " and the computer has chosen "
            + computerChoice
            + "!"
        )

        if playerChoice == computerChoice:
            print("You have tied with the computer!")

        elif playerChoice == "rock" and computerChoice == "scissors":
            print("You have won against the computer!")
        elif playerChoice == "rock" and computerChoice == "paper":
            print("You have lost against the computer!")

        elif playerChoice == "scissors" and computerChoice == "paper":
            print("You have won against the computer!")
        elif playerChoice == "scissors" and computerChoice == "rock":
            print("You have lost against the computer!")

        elif playerChoice == "paper" and computerChoice == "rock":
            print("You have won against the computer!")
        elif playerChoice == "paper" and computerChoice == "scissors":
            print("You have lost against the computer!")

        while True:
            answer = (input("\nRun again? (Y/N): ")).lower()
            while answer != "y" and answer != "n":
                answer = (input("\nRun again? (Y/N): ")).lower()
            if answer == "y":
                startGame()
            else:
                print("Thanks for playing!\n")
                quit()


# ------- Main -------

print("Rock Paper Scissors v.1.0\n-------------------------")
print(
    "\nGame Instructions: \nA simple game in which the player chooses rock, paper or scissors."
    "\nRock defeats scissors, scissors defeats paper, and paper defeats rock!"
    "\nIn this game, you will face against the computer and see who is the champion!"
    "\n-----------------------------------------------------------------------------------------\n"
)

startGame()
