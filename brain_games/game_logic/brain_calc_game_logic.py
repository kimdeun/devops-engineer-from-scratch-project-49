import random

from brain_games.cli import get_user_answer, welcome_user

first_operand = None
second_operand = None
operator = None
name = None


def get_random_number():
    return random.randint(1, 100)


def get_random_operator():
    valid_operators = ["+", "-", "*"]
    return random.choice(valid_operators)


def start_game():
    global name
    name = welcome_user()
    print("What is the result of the expression?")


def question():
    global first_operand
    first_operand = get_random_number()

    global second_operand
    second_operand = get_random_number()

    global operator
    operator = get_random_operator()

    print(f"Question: {first_operand} {operator} {second_operand}")


def is_answer_correct(user_answer):
    match operator:
        case "+":
            return (
                True
                if first_operand + second_operand == int(user_answer)
                else False
            )
        case "-":
            return (
                True
                if first_operand - second_operand == int(user_answer)
                else False
            )
        case "*":
            return (
                True
                if first_operand * second_operand == int(user_answer)
                else False
            )
        case _:
            print("Некорректно выбран оператор")


def get_correct_answer():
    match operator:
        case "+":
            return first_operand + second_operand
        case "-":
            return first_operand - second_operand
        case "*":
            return first_operand * second_operand
        case _:
            print("Некорректно выбран оператор")


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
                f"Correct answer was {get_correct_answer()}\n"
                f"Let's try again, {name}!"
            )
            correct_answer_count = 0


def congrats_user():
    print(f"Congratulations, {name}!")
