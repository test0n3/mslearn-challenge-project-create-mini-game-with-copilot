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
import re

# create an object that shows the relation between options and what they beat.
game_options = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
# ask for user input

# create function get_user_input that asks for user input and returns the input
def get_user_input():
    # create loop to catch user input
    while True:
        user_choice = input("Choose rock, paper or scissors: ").lower()
        # check if user input is valid
        if user_choice not in game_options.keys():
            print("Invalid input.")
        else:
            break            
    return user_choice
    
# create function get_computer_input that returns a random choice from the game_options
def get_computer_input():
    return random.choice(list(game_options.keys()))

# create function try_again that asks the user if they want to play again and returns True or False
def try_again():
    while True:
        play_again = input("Do you want to play again? (Y/N): ").lower()
        if play_again == 'y':
            return True
        elif play_again == 'n':
            return False
        else:
            print("Invalid input.")

# create function game_logic that runs get_user_input, get_computer_input, compares them and returns the result
def game_logic():
    # get user input
    user_choice = get_user_input()
    # get computer input
    computer_choice = get_computer_input()
    # compare user and computer input
    if game_options[user_choice] == computer_choice:
        return 1
    # check if user lost
    elif game_options[computer_choice] == user_choice:
        return -1
    # check if user and computer chose the same
    else:
        return 0


# create function print_message that prints the result of the game
def print_message(result):
    # check if user won
    if result == 1:
        print("You won!")
    # check if user lost
    if result == -1:
        print("You lost!")
    # check if user and computer chose the same
    if result == 0:
        print("It's a draw!")

# create function calculate_score with result and score input that returns the final score
def calculate_score(result, score):
    # check if user won
    if result == 1:
        score += 1
    return score

# create function game that runs the game
def game():
    # create score variable
    score = 0
    games = 0
    play_again = True
    # create loop that runs until user doesn't want to play anymore
    while play_again:
        games += 1
        # run game_logic
        result = game_logic()
        # print result
        print_message(result)
        # calculate score
        score = calculate_score(result, score)
        play_again = try_again()

    # print score
    print(f"Your score is {score}.")
    # print number of games played
    print(f"You played {games} games.")

game()