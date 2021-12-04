from board import Board


def part1(rows):
    numbers, boards = parse_input(rows)
    for number in numbers:
        for board in boards:
            board.mark(number)
        winner = get_winner(boards)
        if (winner):
            return winner.sum_of_remaining() * number
    return None


def part2(rows):
    numbers, boards = parse_input(rows)
    for number in numbers:
        for board in boards:
            board.mark(number)
        new_boards = [board for board in boards if not board.is_winner()]
        if not new_boards:
            return boards[0].sum_of_remaining() * number
        boards = new_boards
    return None


def parse_input(rows):
    numbers = [int(number) for number in rows[0].split(",")]
    boards = list(get_boards(rows))
    return numbers, boards


def get_boards(rows):
    for index in range(2, len(rows), 6):
        yield Board(
            [int(number) for number in row.split()]
            for row
            in rows[index:index+5]
        )


def get_winner(boards):
    for board in boards:
        if board.is_winner():
            return board
    return None
