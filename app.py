# create game logic for a rock, paper, scissors game, the user input and output should be in the console.
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
# If both players choose the same, it's a draw
# 1. Get the user can choose one of the three options rock, paper or scissors and should be warned if they enter an invalid input.
# 2. The computer should also choose randomly between rock, paper and scissors.
# 3. Compare the user's choice and the computer's choice and determine the winner.
# 4. The player must enter one of the options in the list and be informed if they won, lost or tied with the opponent.
# 5. At the end of each round, the player can choose to play again or not.
# 6. Display the player's score at the end of the game.

import random
import os

# create an object that shows the relation between options and what they beat.
options = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
# ask for user input
user_choice = input("Choose rock, paper or scissors: ").lower()
# check if user input is included in the options keys list
while user_choice not in options.keys():
    # clear the console
    os.system('cls')
    # ask for user input again
    user_choice = input("Invalid input. Choose rock, paper or scissors: ").lower()


# computer chooses randomly from the options keys list
computer_choice = random.choice(list(options.keys()))

# print the choices of the user and the computer
print(f"Your choice: {user_choice}")
print(f"Computer's choice: {computer_choice}")

# check if the user won, lost or tied with the computer
if options[user_choice] == computer_choice:
    print("You won!")
elif options[computer_choice] == user_choice:
    print("You lost!")
else:
    print("It's a draw!")




