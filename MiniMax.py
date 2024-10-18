# Mini Max Algorithm 
# Backtracking algorithm
# Best move strategy
# Max will try to maximize its utility ( We will maximize the gain)
# Min will try to minimize  its utlitiy ( opponent will minimize our gain )
# find the best possible move for a player,  assuming the opponent plays optimally, by evaluating future game states.

# So we are Max here 
# we have to maximize the chances of winning 
# and we have to minimize the chance of losing 



import math

# Define a simple game state for Tic-Tac-Toe (3x3 grid)
# 0 represents an empty spot, 1 represents the maximizing player, and -1 represents the minimizing player
def print_board(board):
    for row in board:
        print(row)

def is_moves_left(board):
    # Check if there are any moves left
    for row in board:
        if 0 in row:
            return True
    return False

def evaluate(board):
    # This function check that is any player won 
    # if you wins then it will return 1  ( value stored on board )
    # if opponent wins it will return -1 ( value stored on board )

    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row[0] != 0 and row[0] == row[1] == row[2]:
            return row[0]
    
    for col in range(3):
        if board[0][col] != 0 and board[0][col] == board[1][col] == board[2][col] :
            return board[0][col]
    
    # \ diagonal 1
    if board[0][0] != 0 and board[0][0]  == board[1][1] == board[2][2] :
        return board[0][0]
    
    # / diagonal 2
    if board[0][2] != 0 and  board[0][2] == board[1][1] == board[2][0] :
        return board[0][2]
    
    return 0  # No winner yet

def minimax(board, depth, our_chance):
    score = evaluate(board)

    # If the maximizing player has won, return score
    if score == 1:
        return score
    
    # If the minimizing player has won, return score
    if score == -1:
        return score
    
    # If no more moves and no winner, it's a tie
    if not is_moves_left(board):
        return 0
    
    # Maximizing player's move
    if our_chance: # if value is True 
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 1  # Maximizing player move
                    best = max(best, minimax(board, depth + 1, False)) # here it chooses maximum value between current best and future best
                    board[i][j] = 0  # Undo the move
        return best
    
    # Minimizing player's move
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = -1  # Minimizing player move
                    best = min(best, minimax(board, depth + 1, True)) # it chooses minimum value between current best and future best 
                    board[i][j] = 0  # Undo the move
        return best

def find_best_move(board):
    # negative ifinity 

    best_val = -math.inf # -ve infinity 

    best_move = (-1, -1) # -1, -1 means currently we dont have any best move    
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0: # where ever the spot is empty it is calling minimax function 
                board[i][j] = 1  # Maximizing player's move ( max play ie hum )
                move_val = minimax(board, 0, False) # It will return the payoff value ( jo bhi gain hoga)
                board[i][j] = 0  # Undo the move ( it means we will empty that spot )

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# 0 is an empty spot
# 1 -> you
# -1 -> Opponent

board = [
    [1, 0, 1],
    [1, -1, 0],
    [-1, 1, -1]
]

print("Current board:")
print_board(board)

best_move = find_best_move(board)

print(f"\nThe best move is at position: {best_move}")
