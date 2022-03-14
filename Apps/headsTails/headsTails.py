

import random
from tkinter import N
from time import sleep


play = True

while play:
    def coinFlip():
        global flipResult
        flip = random.randint(1, 2)

        if flip == 1:
            flipResult = "heads"
        else:
            flipResult = "tails"

        return flipResult

    userScore = 0
    cpuScore = 0

    while True:
        try:
            noRounds = int(input("How many rounds would you like to play? "))
        except ValueError:
            print("That was an invalid input, please enter a whole number")
        else:
            break


    round = 1


    while round <= noRounds:
        print("Round: " + str(round))
        while True:
            guess = input("Guess heads or tails: ")
            if guess.lower() not in ("heads", "tails"):
                print("Invalid Input, please enter heads or tails")
            else:
                break
        coinFlip()
        sleep(0.5)
        print("Result was " + flipResult)
        sleep(1)

        if flipResult == guess:
            print("Good Guess!")
            userScore += 1
        else:
            print("Unlucky")
            cpuScore += 1

        sleep(1)
        print("Your current score is " + str(userScore))
        sleep(1)
        print("The computers score is " + str(cpuScore))
        sleep(1)

        round += 1
    sleep(1)
    print("Your final score was " + str(userScore))
    sleep(1)
    print("The computers final score was " + str(cpuScore))
    sleep(1)

    if userScore > cpuScore:
        print("Congrats, you won!")
    elif userScore == cpuScore:
        print("It was a draw")
    else:
        print("Unlucky! You lost")

    while True:
        try:
            playAgain = str(input("Would you like to play again? (Type Y or N)"))
        except ValueError:
            print("Please type Y or N ")
        else:
            break
    
    if playAgain.upper() == "N":
        play = False


