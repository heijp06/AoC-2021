def part1(rows):
    numbers = [int(number) for number in rows[0].split(",")]
    boards = get_boards(rows, 2)
    while True:
        for number in numbers:
            for board_index in range(len(boards) - 1, -1, -1):
                board = boards[board_index]
                for line in board:
                    index = find(line, number)
                    if index > -1:
                        line[index] = -1
            winner = get_winner(boards)
            if (winner):
                return get_result(winner) * number

def find(line, number):
    try:
        return line.index(number)
    except ValueError:
        return -1

def part2(rows):
    numbers = [int(number) for number in rows[0].split(",")]
    boards = get_boards(rows, 2)
    for number in numbers:
        for board_index in range(len(boards) - 1, -1, -1):
            board = boards[board_index]
            for line in board:
                index = find(line, number)
                if index > -1:
                    line[index] = -1
            if is_winner(board):
                boards.remove(board)
                if len(boards) == 0:
                    return get_result(board) * number

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
    if any(line for line in board if all(number == -1 for number in line)):
        return True
    turn = list(zip(*board))
    if any(line for line in turn if all(number == -1 for number in line)):
        return True
    return False


def get_result(board):
    result = 0
    for line in board:
        result += sum(number for number in line if number != -1)
    return result