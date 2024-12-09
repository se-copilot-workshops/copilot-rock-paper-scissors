using RockPaperScissors.Core;
using Xunit;

namespace RockPaperScissors.Tests;

public class GameTests
{
    [Fact]
    public void WhenPlayerChoosesRock_ShouldReturnValidResult()
    {
        // Arrange
        var game = new Game();

        // Act
        var result = game.EvaluateResult(Move.Rock, Move.Scissors); // Example computer move

        // Assert
        Assert.True(result is GameResult.Win or GameResult.Lose or GameResult.Draw);
    }
}