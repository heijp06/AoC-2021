from collections import defaultdict
from game import Game
from universe import Universe


def part1(rows: list[str]) -> int:
    position_player1, position_player2 = parse(rows)
    game = Game(position_player1, position_player2)
    game.play()
    return game.loser.score * game.die.throws


def part2(rows: list[str]) -> int:
    position_player1, position_player2 = parse(rows)
    universes = {Universe(position_player1, position_player2, 0, 0): 1}
    wins1, wins2 = 0, 0
    to_play = 1
    while universes:
        new_universes = defaultdict(int)
        for universe, count in universes.items():
            for new_universe, new_count in universe.turn(to_play):
                if new_universe.score1 >= 21:
                    wins1 += count * new_count
                elif new_universe.score2 >= 21:
                    wins2 += count * new_count
                else:
                    new_universes[new_universe] += count * new_count
        universes = new_universes
        to_play = 3 - to_play
    return max(wins1, wins2)


def parse(rows: list[str]) -> tuple[int, int]:
    position_player1 = int(rows[0].split()[-1])
    position_player2 = int(rows[1].split()[-1])
    return position_player1, position_player2
