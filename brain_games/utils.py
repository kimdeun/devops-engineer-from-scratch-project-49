import random

from brain_games.constants import MAX_RANDOM_NUMBER, MIN_RANDOM_NUMBER


def get_random_number():
    return random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)


def congrats_user(name):
    print(f"Congratulations, {name}!")