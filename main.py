from guess_the_number_functions import *
from art import logo
print(logo)


choose_game_mode = intro()

max_round = determine_max_rounds(choose_game_mode)

for turn in range(max_round):
    print(f"You have {max_round} attempts remaining to guess the number.")
    ask_for_guess = int(input("Make a guess: "))
    checker = guess_check(ask_for_guess, 45)
    if checker == 0:
        break
    max_round -= 1
    if max_round == 0:
        print("You've run out of guesses, you lose.")
        break

