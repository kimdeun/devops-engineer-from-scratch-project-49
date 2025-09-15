import random

from brain_games.cli import get_user_answer, welcome_user
from brain_games.constants import MAX_ATTEMPTS
from brain_games.utils import congrats_user, get_random_number


def get_random_operator():
    valid_operators = ["+", "-", "*"]
    return random.choice(valid_operators)


def start_game():
    name = welcome_user()
    print("What is the result of the expression?")
    return name


def question():
    first_operand = get_random_number()
    second_operand = get_random_number()
    operator = get_random_operator()

    print(f"Question: {first_operand} {operator} {second_operand}")
    return first_operand, second_operand, operator


def calculate(first_operand, second_operand, operator):
    match operator:
        case "+":
            return first_operand + second_operand
        case "-":
            return first_operand - second_operand
        case "*":
            return first_operand * second_operand
        case _:
            print("Некорректно выбран оператор")


def is_answer_correct(user_answer, first_operand, second_operand, operator):
    match operator:
        case "+":
            return (
                True
                if calculate(first_operand, second_operand, operator)
                == int(user_answer)
                else False
            )
        case "-":
            return (
                True
                if calculate(first_operand, second_operand, operator)
                == int(user_answer)
                else False
            )
        case "*":
            return (
                True
                if calculate(first_operand, second_operand, operator)
                == int(user_answer)
                else False
            )
        case _:
            print("Некорректно выбран оператор")


def get_correct_answer(first_operand, second_operand, operator):
    return calculate(first_operand, second_operand, operator)


def validate_user_answer(name):
    correct_answer_count = 0
    while correct_answer_count < MAX_ATTEMPTS:
        first_operand, second_operand, operator = question()
        user_answer = get_user_answer()
        if is_answer_correct(
            user_answer, first_operand, second_operand, operator
        ):
            print("Correct!")
            correct_answer_count += 1
        else:
            correct_answer = get_correct_answer(
                first_operand, second_operand, operator
            )
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!"
            )
            break
    if correct_answer_count == MAX_ATTEMPTS:
        congrats_user(name)
