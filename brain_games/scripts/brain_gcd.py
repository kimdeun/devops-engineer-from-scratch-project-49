from brain_games.game_engine import run_game
from brain_games.game_logic.brain_gcd import get_question_and_answer, task


def main():
    print("Welcome to the Brain Games!")
    run_game(task(), get_question_and_answer)


if __name__ == "__main__":
    main()
