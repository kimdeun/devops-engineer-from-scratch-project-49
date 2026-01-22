import random

from brain_games.constants import (
    MAX_INDEX_OF_MISSED_NUMBER,
    MAX_STEP,
    MIN_INDEX_OF_MISSED_NUMBER,
    MIN_STEP,
    SEQUENCE_MAX_INDEX,
    SEQUENCE_MIN_INDEX,
)
from brain_games.utils import get_random_number


TASK = "What number is missing in the progression?"


def get_question_and_answer():
    first_number = get_random_number()
    index_of_missed_number = random.randint(
        MIN_INDEX_OF_MISSED_NUMBER, MAX_INDEX_OF_MISSED_NUMBER
    )
    step = random.randint(MIN_STEP, MAX_STEP)

    sequence = []
    correct_answer = None

    for i in range(SEQUENCE_MIN_INDEX, SEQUENCE_MAX_INDEX):
        if index_of_missed_number == i:
            sequence.append("..")
            correct_answer = first_number + i * step
        else:
            sequence.append(first_number + i * step)

    question = " ".join(map(str, sequence))
    return question, correct_answer
