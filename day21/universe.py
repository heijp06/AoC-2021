from __future__ import annotations


class Universe:
    def __init__(self, position1: int, position2: int, score1: int, score2: int) -> None:
        self.position1 = position1
        self.position2 = position2
        self.score1 = score1
        self.score2 = score2

    def __key(self) -> tuple[int, int, int, int]:
        return self.position1, self.position2, self.score1, self.score2

    def __hash__(self) -> int:
        return hash(self.__key())

    def __repr__(self) -> str:
        return repr(self.__key())

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Universe) and self.__key() == __o.__key()

    def turn(self, to_play: int) -> list[tuple[Universe, int]]:
        result = []
        for dice_total, count in [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]:
            if to_play == 1:
                position1 = (self.position1 + dice_total) % 10 or 10
                universe = Universe(position1, self.position2,
                                    self.score1 + position1, self.score2)
            else:
                position2 = (self.position2 + dice_total) % 10 or 10
                universe = Universe(self.position1, position2,
                                    self.score1, self.score2 + position2)
            result.append((universe, count))
        return result
