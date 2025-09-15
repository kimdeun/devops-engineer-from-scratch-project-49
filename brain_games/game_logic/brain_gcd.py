from brain_games.cli import get_user_answer, welcome_user
from brain_games.constants import MAX_ATTEMPTS
from brain_games.utils import congrats_user, get_random_number

# first_number = None
# second_number = None
# name = None


def start_game():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    return name


def question():
    first_number = get_random_number()
    second_number = get_random_number()

    print(f"Question: {first_number} {second_number}")
    return first_number, second_number


def get_grc(first_num, second_num):
    a = int(first_num)
    b = int(second_num)

    while b != 0:
        a, b = b, a % b

    return a


def is_answer_correct(user_answer, first_number, second_number):
    return int(user_answer) == get_grc(first_number, second_number)


def validate_user_answer(name):
    correct_answer_count = 0
    while correct_answer_count < MAX_ATTEMPTS:
        first_number, second_number = question()
        user_answer = get_user_answer()
        if is_answer_correct(user_answer):
            print("Correct!")
            correct_answer_count += 1
        else:
            correct_answer = get_grc(first_number, second_number)
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!"
            )
            break
    if correct_answer_count == MAX_ATTEMPTS:
        congrats_user(name)
