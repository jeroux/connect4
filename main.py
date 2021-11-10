import random as rand


def add_token(board, col, player_turn):
    for i, cell in enumerate(board[col]):
        if cell == 0:
            board[col][i] = player_turn
            return i


def random(board):
    col_possible = [i for i, col in enumerate(board) if col[-1] == 0]
    rand.shuffle(col_possible)
    return col_possible[0]


def minmax():
    pass


def player_play(board, player_turn):
    col = random(board)
    #print(col)
    cell = add_token(board, col, player_turn)
    return [col, cell]


def game_over(board, last_move):
    player = board[last_move[0]][last_move[1]]
    col = board[last_move[0]]
    col_num = last_move[0]
    cell_num = last_move[1]

    #start
    if col_num == -1:
        return 0

    #player win

    #vertical
    if cell_num >= 3:
        if col[cell_num-1] == player and col[cell_num-2] == player and col[cell_num-3] == player:
            return 1

    #horizontal
    h = 1
    #droite
    for i in range(1,4):
        if col_num+i < 7:
            if board[col_num+i][cell_num] == player:
                h += 1
            else:
                break
        else:
            break
    if h == 4:
        return 1
    #gauche
    for j in range(1, 5 - h):
        if col_num - j >= 0:
            if board[col_num - j][cell_num] == player:
                h += 1
            else:
                break
        else:
            break

    if h >= 4:
        return 1

    #diagonale
    d = 1
    #descend a droite
    #a droite
    for i in range(1,4):
        if col_num+i < 7 and cell_num-i >= 0:
            if board[col_num+i][cell_num-i] == player:
                d += 1
            else:
                break
        else:
            break

    if d == 4:
        return 1
    #gauche
    for j in range(1, 5 - d):
        if col_num - j >= 0 and cell_num + j < 6:
            if board[col_num - j][cell_num+j] == player:
                d += 1
            else:
                break
        else:
            break

    if d >= 4:
        return 1

    d = 1
    #monte a droite
    # a droite
    for i in range(1, 4):
        if col_num + i < 7 and cell_num + i < 6:
            if board[col_num + i][cell_num + i] == player:
                d += 1
            else:
                break
        else:
            break

    if d == 4:
        return 1
    # gauche
    for j in range(1, 5 - d):
        if col_num - j >= 0 and cell_num - j >= 0:
            if board[col_num - j][cell_num - j] == player:
                d += 1
            else:
                break
        else:
            break

    if d >= 4:
        return 1
    # draw
    if len([i for i, col in enumerate(board) if col[-1] == 0]) == 0:
        return 2

    #game continue
    return 0


def print_board(board):
    tableau = ""
    for row in range(5, -1, -1):
        for col in range(0, 7):
            cell = board[col][row]
            if cell == 1:
                tableau += "O "
            elif cell == -1:
                tableau += "X "
            else:
                tableau += "  "
        tableau += "\n"

    print(tableau)


def game():
    cols, rows = (7, 6)
    board = [[0 for i in range(rows)] for j in range(cols)]
    last_move = (-1, -1)
    winner = 0
    player1 = 1
    player2 = -1
    player_turn = player1

    while not (winner := game_over(board, last_move)):
        last_move = player_play(board, player_turn)
        player_turn *= -1
        #print_board(board)
    """
    if winner == 2:
        print("Draw")
    if winner == 1:
        if player_turn == player1:
            print("Player2 win!")
        else:
            print("Player1 win!")
    """
    return player_turn


if __name__ == '__main__':
    compteur = 0
    for i in range(100000):
        compteur += game()

    print(compteur)
