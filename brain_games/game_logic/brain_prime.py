import math

from brain_games.cli import get_user_answer, welcome_user
from brain_games.constants import MAX_ATTEMPTS
from brain_games.utils import congrats_user, get_random_number


def start_game():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    return name


def question():
    random_number = get_random_number()
    print(f"Question: {random_number}")
    return random_number


def is_prime(random_number):
    if random_number == 1:
        return False
    for i in range(2, int(math.sqrt(random_number)) + 1):
        if random_number % i == 0:
            return False
    return True


def is_answer_correct(user_answer, random_number):
    if (user_answer == "yes" and is_prime(random_number)) or (
        user_answer == "no" and not is_prime(random_number)
    ):
        return True
    else:
        return False


def validate_user_answer(name):
    correct_answer_count = 0
    while correct_answer_count < MAX_ATTEMPTS:
        random_number = question()
        user_answer = get_user_answer()
        if is_answer_correct(user_answer, random_number):
            print("Correct!")
            correct_answer_count += 1
        else:
            prime = is_prime(random_number)
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was {"'yes'" if prime else "'no'"}.\n"
                f"Let's try again, {name}!"
            )
            break
    if correct_answer_count == MAX_ATTEMPTS:
        congrats_user(name)
