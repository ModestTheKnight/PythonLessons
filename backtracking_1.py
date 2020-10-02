def is_valid_board(board, column):
    row = len(board)
    r = 0
    for c in board:
        if column == c or abs(row-r) == abs(column-c):
            return False
        else:
            r += 1

    return True

def print_board(board):
    cell = chr(9633)
    queen = chr(9819)
    for column in board:
        row = list(cell * len(board))
        row[column] = queen
        print(' '.join([str(c) for c in row]))
    print('=' * 2 * len(board))


def n_queens (n, board = None):
    if not board:
        board = []

    if len(board)==n:
        print_board(board)
        count = 1
    else:
        count = 0
        for x in range(n):
            if is_valid_board(board, x):
                board.append(x)
                count += n_queens(n, board)
                board.pop()

    return count

combo_count = n_queens(int(input('>>')))
print (f"Total combination is: {combo_count}")
