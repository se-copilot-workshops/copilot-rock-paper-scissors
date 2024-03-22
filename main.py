from flask import Flask, request, jsonify
import random

CHOICES = ["rock", "paper", "scissors"]

app = Flask(__name__)


def rock_paper_scissors(player_choice):
    if player_choice not in CHOICES:
        raise ValueError("Invalid choice")

    computer_choice = random.choice(CHOICES)

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        result = "You win!"
    else:
        result = "You lose!"

    return computer_choice, result


@app.route("/play", methods=["GET"])
def play():
    user_choice = request.args.get("choice")

    if user_choice not in CHOICES:
        return (
            jsonify(
                {"error": "Invalid choice. Please choose rock, paper, or scissors."}
            ),
            400,
        )

    computer_choice, result = rock_paper_scissors(user_choice)

    return jsonify(
        {
            "user_choice": user_choice,
            "computer_choice": computer_choice,
            "result": result,
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
