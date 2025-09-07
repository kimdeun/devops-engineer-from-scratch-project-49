import random

from brain_games.cli import get_user_answer, welcome_user

first_number_in_progression = None
correct_answer = None
name = None


def get_random_number():
    return random.randint(1, 100)


def get_index_of_missed_number():
    return random.randint(0, 9)


def get_step():
    return random.randint(2, 7)


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

    for i in range(0, 9):
        if index_of_missed_number == i:
            sequence.append("..")
            global correct_answer
            correct_answer = first_number + i * step
        else:
            sequence.append(first_number + i * step)

    print(f"Question: {' '.join(map(str, sequence))}")


def is_answer_correct(user_answer):
    if isinstance(user_answer, int):
        return int(user_answer) == correct_answer
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
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!"
            )
            break
    if correct_answer_count == 3:
        congrats_user()


def congrats_user():
    print(f"Congratulations, {name}!")
