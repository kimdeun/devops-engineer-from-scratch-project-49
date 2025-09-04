from brain_games.game_logic.brain_calc_game_logic import (
    congrats_user,
    start_game,
    validate_user_answer,
)


def main():
    print("Welcome to the Brain Games!")
    start_game()
    validate_user_answer()
    congrats_user()


if __name__ == "__main__":
    main()
