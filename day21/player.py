from deterministic_die import DeterministicDie


class Player:
    def __init__(self, position: int, die: DeterministicDie) -> None:
        self.position = position
        self.die = die
        self.score = 0
    
    def __repr__(self) -> str:
        return f"{self.position}, {self.score}"
    
    def turn(self) -> None:
        total = self.die.throw() + self.die.throw() + self.die.throw()
        self.position += total
        self.position %= 10
        if self.position == 0:
            self.position = 10
        self.score += self.position