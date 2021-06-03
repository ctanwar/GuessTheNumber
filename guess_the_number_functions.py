def intro():
    """
    Prints intro text and asks user to choose game mode.
    :return: User's input
    """
    print("Welcome to the Number Guessing Game!\n"
          "I'm thinking of a number between 1 and 100.")
    return input("Choose a difficulty. Type 'hard' or game plays on easy by default: ")


def determine_max_rounds(_game_difficulty):
    """
    Game defaults to easy mode unless user enters 'hard'.
    :param _game_difficulty:
    :return: 5 for hard mode, 10 easy mode
    """
    if _game_difficulty == "hard":
        return 5
    else:
        return 10


def guess_check(_guess, _answer):
    """
    Evaluates and prints statement based on user's guess.
    :param _guess:
    :param _answer:
    :return: 2 if high, 1 if low, 0 if equal
    """
    if _guess > _answer:
        print("Too high.")
        return 2
    elif _guess < _answer:
        print("Too low.")
        return 1
    else:
        print(f"You got it! The answer was {_answer}")
        return 0

