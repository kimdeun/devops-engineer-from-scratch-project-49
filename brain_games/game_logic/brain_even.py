import random

from brain_games.cli import get_user_answer, welcome_user
from brain_games.constants import (
    MAX_ATTEMPTS,
    MAX_RANDOM_NUMBER,
    MIN_RANDOM_NUMBER,
)
from brain_games.steps import congrats_user

name = None
random_number = None


def get_random_number():
    return random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)


def start_game():
    global name
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')


def question():
    global random_number
    random_number = get_random_number()
    print(f"Question: {random_number}")


def is_answer_correct(user_answer):
    if (user_answer == "yes" and random_number % 2 == 0) or (
        user_answer == "no" and random_number % 2 != 0
    ):
        return True
    else:
        return False


def validate_user_answer():
    correct_answer_count = 0
    while correct_answer_count < MAX_ATTEMPTS:
        question()
        user_answer = get_user_answer()
        if is_answer_correct(user_answer):
            print("Correct!")
            correct_answer_count += 1
        else:
            correct_answer = "'yes'" if user_answer == "no" else "'no'"
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was {correct_answer}.\n"
                f"Let's try again, {name}!"
            )
            break
    if correct_answer_count == MAX_ATTEMPTS:
        congrats_user(name)
