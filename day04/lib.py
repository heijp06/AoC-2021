def part1(rows):
    numbers = [int(number) for number in rows[0].split(",")]
    boards = get_boards(rows, 2)
    while True:
        for number in numbers:
            for board in boards:
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
    pass


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
        if any(line for line in board if all(number == -1 for number in line)):
            return board
        turn = list(zip(*board))
        if any(line for line in turn if all(number == -1 for number in line)):
            return board
        # diagonal = True
        # for index in range(5):
        #     if board[index][index] != -1:
        #         diagonal = False
        # if diagonal:
        #     return board
        # diagonal = True
        # for index in range(5):
        #     if board[index][4 - index] != -1:
        #         diagonal = False
        # if diagonal:
        #     return board
    return None

def get_result(board):
    result = 0
    for line in board:
        result += sum(number for number in line if number != -1)
    return result