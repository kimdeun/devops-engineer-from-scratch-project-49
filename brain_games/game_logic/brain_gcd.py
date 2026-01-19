from brain_games.utils import get_random_number


def task():
    return "Find the greatest common divisor of given numbers."


def get_gcd(first_num, second_num):
    a = int(first_num)
    b = int(second_num)

    while b != 0:
        a, b = b, a % b

    return a


def get_question_and_answer():
    first_number = get_random_number()
    second_number = get_random_number()

    question = f"{first_number} {second_number}"
    correct_answer = get_gcd(first_number, second_number)

    return question, correct_answer
