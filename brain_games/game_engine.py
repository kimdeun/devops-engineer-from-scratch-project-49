from brain_games.cli import get_user_answer, welcome_user
from brain_games.constants import MAX_ATTEMPTS
from brain_games.utils import congrats_user


def run_game(task, get_question_and_answer):
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print(task)

    correct_answer_count = 0
    while correct_answer_count < MAX_ATTEMPTS:
        question, correct_answer = get_question_and_answer()
        print(f"Question: {question}")
        user_answer = get_user_answer()

        if str(user_answer) == str(correct_answer):
            print("Correct!")
            correct_answer_count += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!"
            )
            return

    if correct_answer_count == MAX_ATTEMPTS:
        congrats_user(name)
