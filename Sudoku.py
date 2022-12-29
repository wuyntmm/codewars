def valid_solution(board):
    result = True
    for horizontal in board:
        temp_set = set(horizontal)
        if len(temp_set) != 9:
            result = False
    for vert in map(list, zip(*board)):
        temp_set = set(vert)
        if len(temp_set) != 9 or 0 in temp_set:
            result = False
    temp = []
    temp_set = set()
    y_move = 0
    x_move = 0
    for y_move in range(0, 7, 3):
        temp = []
        for x_move in range(0, 7, 3):
            temp = []
            for y in range(y_move, y_move + 3):
                for x in range(x_move, x_move + 3):
                    temp.append(board[y][x])
                    if len(temp) == 9:
                        print(temp)
                        temp_set = set(temp)
                        if len(temp_set) != 9 or 0 in temp_set:
                            result = False

    return result


print(valid_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                         , [4, 9, 8, 2, 6, 1, 3, 7, 5]
                         , [7, 5, 6, 3, 8, 4, 2, 1, 9]
                         , [6, 4, 3, 1, 5, 8, 7, 9, 2]
                         , [5, 2, 1, 7, 9, 3, 8, 4, 6]
                         , [9, 8, 7, 4, 2, 6, 5, 3, 1]
                         , [2, 1, 4, 9, 3, 5, 6, 8, 7]
                         , [3, 6, 5, 8, 1, 7, 9, 2, 4]
                         , [8, 7, 9, 6, 4, 2, 1, 5, 3]]))
