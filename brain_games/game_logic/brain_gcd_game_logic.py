import random

from brain_games.cli import get_user_answer, welcome_user


first_number = None
second_number = None
naem = None

def get_random_number():
    return random.randint(1, 100)

def start_game():
    global name
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')

def question():
    global first_number
    first_number = get_random_number()

    global second_number
    second_number = get_random_number()

    print(f"Question: {first_number} {second_number}")  

def get_grc(first_num, second_num):
    a = int(first_num)
    b = int(second_num)

    while (b != 0):
        a, b = b, a % b

    return a
    
def is_answer_correct(user_answer):
    return int(user_answer) == get_grc(first_number, second_number)

def validate_user_answer():
    correct_answer_count = 0
    while correct_answer_count < 3:
        question()
        user_answer = get_user_answer()
        if (is_answer_correct(user_answer)):
            print("Correct!")
            correct_answer_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was {get_grc(first_number, second_number)}\nLet's try again, {name}!")
            correct_answer_count = 0

def congrats_user():
    print(f"Congratulations, {name}!")