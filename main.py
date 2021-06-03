from guess_the_number_functions import *
from art import logo
import random

print(logo)

# Computer generated random number from 1-100.
rng = random.randint(1, 100)
print(f"Backdoor: {rng}")

# Player chooses 'easy' or 'hard'; bad inputs default game to easy mode.
choose_game_mode = intro()

# Determines number of game rounds based on game mode.
max_round = determine_max_rounds(choose_game_mode)

# Basic game engine; loops until player answers correctly or until number of rounds depleted.
for turn in range(max_round):
    print(f"You have {max_round} attempts remaining to guess the number.")
    ask_for_guess = int(input("Make a guess: "))
    checker = guess_check(ask_for_guess, rng)
    if checker == 0:
        break
    max_round -= 1
    if max_round >= 1:
        print("Guess again.")
    if max_round == 0:
        print("You've run out of guesses, you lose.")
        break

