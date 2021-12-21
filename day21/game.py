from deterministic_die import DeterministicDie
from player import Player


class Game:
    def __init__(self, position_player1: int, position_player2: int) -> None:
        self.die = DeterministicDie()
        self.player1 = Player(position_player1, self.die)
        self.player2 = Player(position_player2, self.die)
        self.winner = None
        self.loser = None
    
    def __repr__(self) -> str:
        return f"P1: {self.player1}, P2: {self.player2}, Die: {self.die}"

    def play(self) -> None:
        player, other = self.player1, self.player2
        while other.score < 1000:
            player.turn()
            player, other = other, player
        self.winner = other
        self.loser = player