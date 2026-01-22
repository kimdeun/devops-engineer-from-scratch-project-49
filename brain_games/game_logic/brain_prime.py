import math

from brain_games.constants import MIN_PRIME_NUMBER, PRIME_CHECK_START
from brain_games.utils import get_random_number


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(random_number):
    if random_number == MIN_PRIME_NUMBER:
        return False
    for i in range(PRIME_CHECK_START, int(math.sqrt(random_number)) + 1):
        if random_number % i == 0:
            return False
    return True


def get_question_and_answer():
    random_number = get_random_number()
    correct_answer = "yes" if is_prime(random_number) else "no"
    return random_number, correct_answer
