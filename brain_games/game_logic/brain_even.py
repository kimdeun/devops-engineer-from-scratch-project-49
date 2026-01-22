from brain_games.utils import get_random_number


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    random_number = get_random_number()
    correct_answer = "yes" if random_number % 2 == 0 else "no"
    return random_number, correct_answer
