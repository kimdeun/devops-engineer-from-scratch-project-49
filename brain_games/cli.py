import prompt


def welcome_user():
    name = prompt.string("May I have your name? \n")
    print(f"Hello, {name}!")
    return name


def get_user_answer():
    answer = prompt.string("Your answer: ")
    return answer
