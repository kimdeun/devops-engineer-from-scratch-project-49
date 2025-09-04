import math
import random

from brain_games.cli import get_user_answer, welcome_user

name = None
random_number = None


def get_random_number():
    return random.randint(1, 100)


def start_game():
    global name
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def question():
    global random_number
    random_number = get_random_number()
    print(f"Question: {random_number}")


def is_prime():
    if random_number == 1:
        return False
    for i in range(2, int(math.sqrt(random_number)) + 1):
        if random_number % i == 0:
            return False
    return True


def is_answer_correct(user_answer):
    if (user_answer == "yes" and is_prime()) or (
        user_answer == "no" and not is_prime()
    ):
        return True
    else:
        return False


def validate_user_answer():
    correct_answer_count = 0
    while correct_answer_count < 3:
        question()
        user_answer = get_user_answer()
        if is_answer_correct(user_answer):
            print("Correct!")
            correct_answer_count += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was {'\'yes\'' if is_prime() else '\'no\''}.\n"
                f"Let's try again, {name}!"
            )
            correct_answer_count = 0


def congrats_user():
    print(f"Congratulations, {name}!")
