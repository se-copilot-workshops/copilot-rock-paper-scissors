using Microsoft.AspNetCore.Mvc;
using RockPaperScissors.Core;

namespace RockPaperScissors.Api.Controllers;

[ApiController]
[Route("[controller]")]
public class GameController : ControllerBase
{
    private readonly IGame _game;

    public GameController(IGame game)
    {
        _game = game;
    }

    [HttpGet("play")]
    public IActionResult Play([FromQuery] Move move)
    {
        throw new NotImplementedException("Implement the API endpoint here");
    }
}