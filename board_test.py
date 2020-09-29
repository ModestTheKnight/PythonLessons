def is_valid_board(board, column):
    row = len(board)
    r = 0
    for c in board:
        if column == c or abs(row-r) == abs(column-c):
            return False
        else:
            r += 1

    return True

alist = [int(x) for x in input('board>>').split()]
pos = int(input('column>>'))
if is_valid_board(alist,pos):
    print('valid')
else:
    print('invalid')
