# Hangman
# Made by TheQuantumRobot

# ------- Modules -------

import random

# ------- Main -------


def startGame():
    print(
        "HANGMAN!\n--------\n\n"
        "Description and Rules\n---------------------\n"
        "In Hangman, the goal is to guess the word or phrase before the man gets hung."
        "\nThe player guessing has six turns before they lose! Good luck!\n\n"
        "Notable Things:\n"
        "     - All words will only have alphabetical letters.\n"
        #       "     - Type HINT for a hint.\n"
        #       "     - Type GUESSED LETTERS to view all guessed letters.\n"
        #       "     - Type FINAL GUESS to final guess. After you final guess, the game is over!\n"
    )

    input("Press enter to continue...\n")

    print(
        "Choose Gamemode\n---------------\n"
        "\nEnter 1 for Player vs Player"
        "\nEnter 2 for Player vs Computer\n"
    )

    playerChoice = int(input("Please choose game mode: "))
    while playerChoice != 1 and playerChoice != 2:
        try:
            playerChoice = int(input("Please choose game mode: "))
        except ValueError:
            playerChoice = int(input("Please choose game mode: "))

    # ------- Hangman Functions and Variables -------
    def randomLine(filename):
        line = open(filename).read().splitlines()
        return random.choice(line).upper()

    chosenWord = randomLine("misc/hangmanwordlist.txt")

    playerAttempts = 0
    playerWon = False
    guessedLetters = []
    guessedWords = []
    playerGuess = ""
    dashedLines = len(chosenWord) * "-"

    def hangmanStages(tries):
        stages = [
            r"""
                      +---+
                      |   |
                          |
                          |
                          |
                          |
                    =========
            """,
            r"""
                      +---+
                      |   |
                      O   |
                          |
                          |
                          |
                    =========
            """,
            r"""
                      +----
                      |   |
                      O   |
                      |   |
                          |
                          |
                    =========
            """,
            r"""
                      +---+
                      |   |
                      O   |
                     /|   |
                          |
                          |
                    =========
            """,
            r"""
                      +---+
                      |   |
                      O   |
                     /|\  |
                          |
                          |
                     =========
            """,
            r"""
                      +---+
                      |   |
                      O   |
                     /|\  |
                     /    |
                          |
                    =========
            """,
            r"""
                      +---+
                      |   |
                      O   |
                     /|\  |
                     / \  |
                          |
                    =========
            """,
        ]
        return stages[tries]

    # ------- Main Cont. --------

    if playerChoice == 1:
        print("Player vs Player\n----------------\n")
        #       playerOneWord = input("Player 1's Phrase: ").lower()
        print("Player vs Player Gamemode is under construction!")

    if playerChoice == 2:
        print("Player vs Computer\n------------------\n")
        while (playerWon == False) and (playerAttempts < 6):
            print(hangmanStages(playerAttempts))
            print(dashedLines + "\n")
            playerGuess = input("Please guess a letter / word: ").upper()
            if (len(playerGuess) == 1) and (playerGuess.isalpha()):
                if playerGuess in guessedLetters:
                    print(playerGuess + " has already been guessed.")
                elif playerGuess not in chosenWord:
                    print(playerGuess + " is not in the word!")
                    playerAttempts += 1
                    guessedLetters.append(playerGuess)
                else:
                    print(playerGuess + " is in the word! Congrats!")
                    guessedLetters.append(playerGuess)
                    word_as_list = list(dashedLines)
                    indices = [
                        i
                        for i, letter in enumerate(chosenWord)
                        if letter == playerGuess
                    ]
                    for index in indices:
                        word_as_list[index] = playerGuess
                    dashedLines = "".join(word_as_list)
                    if "-" not in dashedLines:
                        playerWon = True

            if playerGuess == chosenWord and playerGuess.isalpha():
                if playerGuess in guessedWords:
                    print(playerGuess + " has already been guessed.")

                elif playerChoice != chosenWord:
                    print(playerGuess + " is not in the word!")
                    playerAttempts += 1
                    guessedWords.append(playerGuess)
                else:
                    print(playerGuess + " is in the chosen word!")
                    playerWon = True
                    input("Press any key to end the game: ")
        if playerWon:
            print(
                "Congrats! You've guessed the word "
                + chosenWord
                + ". You've saved the man!"
            )
            quit()
        else:
            print(
                "Oops! You ran out of guesses. The word was "
                + chosenWord
                + ". The man died. : ("
            )


startGame()
