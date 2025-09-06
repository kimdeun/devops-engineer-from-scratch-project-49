from brain_games.game_logic.brain_progression_game_logic import (
    start_game,
    validate_user_answer,
)


def main():
    print("Welcome to the Brain Games!")
    start_game()
    validate_user_answer()


if __name__ == "__main__":
    main()
