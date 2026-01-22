from brain_games.game_engine import run_game
from brain_games.game_logic.brain_calc import TASK, get_question_and_answer


def main():
    run_game(TASK, get_question_and_answer)


if __name__ == "__main__":
    main()
