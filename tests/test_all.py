import pytest
from unittest.mock import patch
from main import rock_paper_scissors


def test_invalid_choice():
    with pytest.raises(ValueError):
        rock_paper_scissors("invalid")


@patch("random.choice", return_value="rock")
def test_rock(mock_choice):
    assert rock_paper_scissors("rock") == "It's a tie!"
    assert rock_paper_scissors("paper") == "You win!"
    assert rock_paper_scissors("scissors") == "You lose!"


@patch("random.choice", return_value="paper")
def test_paper(mock_choice):
    assert rock_paper_scissors("rock") == "You lose!"
    assert rock_paper_scissors("paper") == "It's a tie!"
    assert rock_paper_scissors("scissors") == "You win!"


@patch("random.choice", return_value="scissors")
def test_scissors(mock_choice):
    assert rock_paper_scissors("rock") == "You win!"
    assert rock_paper_scissors("paper") == "You lose!"
    assert rock_paper_scissors("scissors") == "It's a tie!"
