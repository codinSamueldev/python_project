import random

def get_computer_choice():
    """Get a random option for the computer to use."""
    return random.choice(options)

def get_user_choice():
    """Get the option the player will use."""
    user = input("Select what you want to play this round: Rock, paper, scissors.\n").lower()
    if user in options:
        return user
    else:
        raise ValueError("Your choice is not valid. Check for typos and try again.")

def determine_winner(user, computer):
    """Determine the winner for a round."""
    if user == computer:
        return "It's a tie!", None
    elif (user == "scissors" and computer == "paper") or (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock"):
        return f"You have won this round! {user} beats {computer}!", True
    else:
        return f"You have lost this round. {computer} beats {user}!", False

def run_game():
    """Start and handle the game from start to finish."""
    rounds = 3
    user_wins = 0
    computer_wins = 0

    print("*" * 15)
    print("The game will start now.")
    print("*" * 15)

    while rounds >= 0:
        computer = get_computer_choice()
        user = get_user_choice()

        result, user_won = determine_winner(user, computer)
        print(result)

        rounds -= 1

        if user_won is not None:
            if user_won:
                user_wins += 1
            else:
                computer_wins += 1

    print("\nGame Over!")
    if user_wins == computer_wins:
        print("It's a tie, you ended the game with the same amount of points.")
    elif user_wins > computer_wins:
        print(f"Match ended. You are the winner with {user_wins} points!")
    else:
        print(f"Match ended. The winner is the computer with {computer_wins} points.")

if __name__ == "__main__":
    # Global choice options.
    options = ("rock", "paper", "scissors")
    run_game()
