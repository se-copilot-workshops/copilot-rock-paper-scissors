namespace RockPaperScissors.Core;

public enum Move
{
    Rock,
    Paper,
    Scissors
}

public enum GameResult
{
    Win,
    Lose,
    Draw
}

public interface IGame
{
    GameResult EvaluateResult(Move playerMove, Move computerMove);
}

public class Game : IGame
{
    public GameResult EvaluateResult(Move playerMove, Move computerMove)
    {
        throw new NotImplementedException("Implement the game logic here");
    }
}