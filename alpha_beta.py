# Alpha-Beta Pruning is an optimization of Mini-Max that skips parts of the search tree 
# that won't affect the final decision, improving efficiency by pruning irrelevant branches.

# Alpha-Beta Pruning reduces the number of nodes evaluated in the game tree
#  while Mini-Max checks all nodes without skipping any.

import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(row)
    print()

# Check if the game is over
def is_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if row == [player, player, player]:
            return True
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Check if the board is full (draw)
def is_draw(board):
    for row in board:
        if 0 in row:  # Check for empty spots
            return False
    return True

# Mini-Max function with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    print('----------------------------------------')
    if is_winner(board, 1):
        return 1  # Max player (1) wins
    if is_winner(board, -1):
        return -1  # Min player (-1) wins
    if is_draw(board):
        return 0  # Draw

    if is_maximizing:
        print("our player chances")

        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:  # Empty spot
                    board[i][j] = 1  # Max player move
                    print(f"max player move : {i},{j} - board : ")
                    print_board(board)
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = 0  # Undo move
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    print(f" our beta : {beta} , alpha : {alpha}")
                    if beta <= alpha:
                        print('our if true beta cut off')
                        break  # Beta cut-off
        return max_eval
    else:
        print("Opponent player chances")
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:  # Empty spot
                    board[i][j] = -1  # Min player move
                    print(f" min player move : {i},{j} - board : ")
                    print_board(board)
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = 0  # Undo move
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    print(f" use beta : {beta} , alpha : {alpha}")

                    if beta <= alpha:
                        print('oppo if true alpha cut off  ')
                        break  # Alpha cut-off
        return min_eval

# Find the best move for the maximizing player (1)
def best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:  # Empty spot
                board[i][j] = 1  # Max player move
                print(f" ( initial ) max player move : {i},{j} - board : ")
                print_board(board)
                # minimax ( board, depth, our chance, alpha, beta)
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = 0  # Undo move
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

# Initial board configuration
board = [
    [1, 0, 0],
    [1, -1, 0],
    [-1, 1, -1]
]

# Display the current board
print("Current Board:")
print_board(board)

# Find and print the best move for player 1
move = best_move(board)
print(f"The best move for player 1 is at position: {move}")
