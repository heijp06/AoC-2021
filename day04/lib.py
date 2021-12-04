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
    boards = list(get_boards(rows, 2))
    return numbers, boards


def get_boards(rows, index):
    while index < len(rows) - 1:
        board_rows = []
        for row in rows[index:index+5]:
            board_row = [int(number) for number in row.split()]
            board_rows.append(board_row)
            index += 1
            yield Board(board_rows)
        index += 1


def get_winner(boards):
    for board in boards:
        if board.is_winner():
            return board
    return None
