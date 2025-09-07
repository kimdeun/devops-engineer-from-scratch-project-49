import random

from brain_games.cli import get_user_answer, welcome_user
from brain_games.constants import (
    MAX_ATTEMPTS,
    MAX_INDEX_OF_MISSED_NUMBER,
    MAX_STEP,
    MIN_INDEX_OF_MISSED_NUMBER,
    MIN_STEP,
    SEQUENCE_MAX_INDEX,
    SEQUENCE_MIN_INDEX,
)
from brain_games.steps import congrats_user, get_random_number

first_number_in_progression = None
correct_answer = None
name = None


def get_index_of_missed_number():
    return random.randint(MIN_INDEX_OF_MISSED_NUMBER, 
                          MAX_INDEX_OF_MISSED_NUMBER)


def get_step():
    return random.randint(MIN_STEP, MAX_STEP)


def start_game():
    global name
    name = welcome_user()
    print("What number is missing in the progression?")


def question():
    global first_number_in_progression
    first_number = get_random_number()

    index_of_missed_number = get_index_of_missed_number()

    step = get_step()

    sequence = []

    for i in range(SEQUENCE_MIN_INDEX, SEQUENCE_MAX_INDEX):
        if index_of_missed_number == i:
            sequence.append("..")
            global correct_answer
            correct_answer = first_number + i * step
        else:
            sequence.append(first_number + i * step)

    print(f"Question: {' '.join(map(str, sequence))}")


def is_answer_correct(user_answer):
    if not user_answer.isdigit():
        return False
    else:
        return int(user_answer) == correct_answer


def validate_user_answer():
    correct_answer_count = 0
    while correct_answer_count < MAX_ATTEMPTS:
        question()
        user_answer = get_user_answer()
        if is_answer_correct(user_answer):
            print("Correct!")
            correct_answer_count += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!"
            )
            break
    if correct_answer_count == MAX_ATTEMPTS:
        congrats_user(name)
