import random

from brain_games.constants import OPERATORS
from brain_games.utils import get_random_number


TASK = "What is the result of the expression?"


def calculate(first_operand, second_operand, operator):
    match operator:
        case "+":
            return first_operand + second_operand
        case "-":
            return first_operand - second_operand
        case "*":
            return first_operand * second_operand
        case _:
            raise ValueError("Некорректно выбран оператор")


def get_question_and_answer():
    first_operand = get_random_number()
    second_operand = get_random_number()
    operator = random.choice(OPERATORS)

    question = f"{first_operand} {operator} {second_operand}"
    correct_answer = calculate(first_operand, second_operand, operator)

    return question, correct_answer
