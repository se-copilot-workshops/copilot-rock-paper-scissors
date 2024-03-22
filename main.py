import random


def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    user_choice = input("Enter your choice (rock, paper, scissors): ")
    while user_choice not in choices:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock, paper, scissors): ")

    print("Computer chose: ", computer_choice)

    if user_choice == computer_choice:
        return "It's a tie!"
    if (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "You lose!"


def main():
    print(rock_paper_scissors())


if __name__ == "__main__":
    main()
