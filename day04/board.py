from itertools import chain


class Board:
    def __init__(self, rows):
        self.rows = rows

    def sum_of_remaining(self):
        return sum(
            sum(number for number in row if number is not None)
            for row
            in self.rows
        )

    def is_winner(self):
        return any(
            row
            for row
            in chain(self.rows, zip(*self.rows))
            if all(number is None for number in row)
        )

    def mark(self, number):
        for row in self.rows:
            if number in row:
                index = row.index(number)
                row[index] = None
