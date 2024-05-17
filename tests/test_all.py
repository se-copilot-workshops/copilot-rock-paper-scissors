import pytest
from unittest.mock import patch
from main import rock_paper_scissors


def test_invalid_choice():
    with pytest.raises(ValueError):
        rock_paper_scissors("invalid")


@patch("random.choice", return_value="rock")
def test_rock(mock_choice):
    assert rock_paper_scissors("rock") == ("rock", "It's a tie!")
    assert rock_paper_scissors("paper") == ("rock", "You win!")
    assert rock_paper_scissors("scissors") == ("rock", "You lose!")


@patch("random.choice", return_value="paper")
def test_paper(mock_choice):
    assert rock_paper_scissors("rock") == ("paper", "You lose!")
    assert rock_paper_scissors("paper") == ("paper", "It's a tie!")
    assert rock_paper_scissors("scissors") == ("paper", "You win!")


@patch("random.choice", return_value="scissors")
def test_scissors(mock_choice):
    assert rock_paper_scissors("rock") == ("scissors", "You win!")
    assert rock_paper_scissors("paper") == ("scissors", "You lose!")
    assert rock_paper_scissors("scissors") == ("scissors", "It's a tie!")
