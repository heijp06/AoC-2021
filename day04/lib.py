from itertools import chain


def part1(rows):
    numbers, boards = parse_input(rows)
    for number in numbers:
        for board in boards:
            for line in board:
                index = line.index(number) if number in line else -1
                if index > -1:
                    line[index] = -1
        winner = get_winner(boards)
        if (winner):
            return get_result(winner) * number
    return -1


def part2(rows):
    numbers, boards = parse_input(rows)
    for number in numbers:
        for board_index in range(len(boards) - 1, -1, -1):
            board = boards[board_index]
            for line in board:
                index = line.index(number) if number in line else -1
                if index > -1:
                    line[index] = -1
            if is_winner(board):
                boards.remove(board)
                if not boards:
                    return get_result(board) * number

def parse_input(rows):
    numbers = [int(number) for number in rows[0].split(",")]
    boards = get_boards(rows, 2)
    return numbers, boards

def get_boards(rows, index):
    boards = []
    last = len(rows) - 4
    while(index < last):
        board = []
        for line in range(5):
            line = [int(number) for number in rows[index].split()]
            board.append(line)
            index += 1
        boards.append(board)
        index += 1
    return boards


def get_winner(boards):
    for board in boards:
        if is_winner(board):
            return board
    return None


def is_winner(board):
    return any(
        line
        for line
        in chain(board, zip(*board))
        if all(number == -1 for number in line)
    )


def get_result(board):
    return sum(sum(number for number in line if number != -1) for line in board)
