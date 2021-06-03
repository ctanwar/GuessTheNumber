def intro():
    print("Welcome to the Number Guessing Game!\n"
          "I'm thinking of a number between 1 and 100.")
    return input("Choose a difficulty. Type 'hard' or game plays on easy by default: ")


def determine_max_rounds(_game_difficulty):
    if _game_difficulty == "hard":
        return 5
    else:
        return 10


def guess_check(_guess, _answer):
    if _guess > _answer:
        print("Too high.\nGuess again.")
        return 2
    elif _guess < _answer:
        print("Too low.\nGuess again.")
        return 1
    else:
        print(f"You got it! The answer was {_answer}")
        return 0

