from brain_games.brain_even_game_logic import congrats_user, question, start_game, validate_user_answer
from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    start_game()
    validate_user_answer()
    congrats_user()

if __name__ == "__main__":
    main()
