from game import Game


def part1(rows: list[str]) -> int:
    player1 = int(rows[0].split()[-1])
    player2 = int(rows[1].split()[-1])
    game = Game(player1, player2)
    game.play()
    return game.loser.score * game.die.throws


def part2(rows):
    pass
