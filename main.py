from flask import Flask, request, jsonify
import random

app = Flask(__name__)


@app.route("/play", methods=["GET"])
def play():
    user_choice = request.args.get("choice")
    choices = ["rock", "paper", "scissors"]

    if user_choice not in choices:
        return (
            jsonify(
                {"error": "Invalid choice. Please choose rock, paper, or scissors."}
            ),
            400,
        )

    computer_choice = random.choice(choices)
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        result = "You win!"
    else:
        result = "You lose!"

    return jsonify(
        {
            "user_choice": user_choice,
            "computer_choice": computer_choice,
            "result": result,
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
