class DeterministicDie:
    def __init__(self) -> None:
        self.value = 1
        self.throws = 0
    
    def __repr__(self) -> str:
        return f"{self.value}, {self.throws}"

    def throw(self) -> int:
        value = self.value
        self.value += 1
        if self.value == 101:
            self.value = 1
        self.throws += 1
        return value
