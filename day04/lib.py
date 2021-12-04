from board import Board
import sys


def part1(rows):
    numbers, boards = parse_input(rows)
    for number in numbers:
        for board in boards:
            board.mark(number)
        winner = get_winner(boards)
        if winner:
            return winner.sum_of_remaining() * number
    return None


def part2(rows):
    numbers, boards = parse_input(rows)
    img = 0
    org_boards = list(boards)
    print_boards(org_boards, boards, img)
    img += 1
    for number in numbers:
        for board in boards:
            board.mark(number)
        print_boards(org_boards, boards, img)
        img += 1
        new_boards = [board for board in boards if not board.is_winner()]
        if not new_boards:
            return boards[0].sum_of_remaining() * number
        boards = new_boards
    return None


def print_boards(org_boards, boards, img):
    stdout = sys.stdout
    with open(f"img/img{img:03d}.txt", "w") as f:
        sys.stdout = f
        if len(org_boards) != 100:
            return
        rows = 8
        columns = 13
        for row in range(rows):
            if row:
                print()
            for board_row in range(5):
                for column in range(columns):
                    index = row * columns + column
                    if index >= 100:
                        continue
                    if column:
                        print("  ", end='')
                    board = org_boards[index]
                    if board in boards:
                        print_row(board.rows[board_row])
                    else:
                        print_row([None] * 5)
                print()
    sys.stdout = stdout


def print_row(row):
    show = [
        " " if number is None else number
        for number
        in row
    ]
    print(f"{show[0]:>2} {show[1]:>2} {show[2]:>2} {show[3]:>2} {show[4]:>2}", end='')


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
