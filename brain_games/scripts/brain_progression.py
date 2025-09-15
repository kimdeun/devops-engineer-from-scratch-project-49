from brain_games.game_logic.brain_progression import (
    start_game,
    validate_user_answer,
)


def main():
    print("Welcome to the Brain Games!")
    validate_user_answer(start_game())


if __name__ == "__main__":
    main()
