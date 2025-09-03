from brain_games.game_logic.brain_prime_game_logic import start_game, validate_user_answer, congrats_user


def main():
    print("Welcome to the Brain Games!")
    start_game()
    validate_user_answer()
    congrats_user()

if __name__ == "__main__":
    main()
