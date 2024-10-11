import random

def get_user_choice():
    while True:
        user_choice = input("There are 3 choices overall: Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    print(f"You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")

    for _ in range(3):  # Three chances
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1

    print("\nGame Over!")
    print(f"Your score: {user_score}")
    print(f"Computer's score: {computer_score}")

    if user_score > computer_score:
        print("Congratulations! You are the overall winner!")
    elif user_score < computer_score:
        print("Sorry, the computer is the overall winner.")
    else:
        print("It's a tie overall!")

# Play the game
play_game()
