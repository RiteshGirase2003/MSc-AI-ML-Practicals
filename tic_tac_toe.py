# Tic-Tac-Toe Game

# Initialize an empty 3x3 board
board = [ [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def print_board():
    """Prints the current state of the board"""
    print('-' * 5)
    for row in board:
        print(row)
    print('-' * 5)

def check_row(player, row):
    """Checks if the player has won in the row"""
    r = board[row]
    for i in r:
        if i != player: 
            return False
    
    return True
    # return all([board[row][col] == player for col in range(3)])

def check_col(player, col):
    """Checks if the player has won in the column"""
    for row in board:
        if row[col] != player:
            return False
        
    return True

    
    # return all([board[row][col] == player for row in range(3)])

def check_diag1(player):
    """Checks if the player has won in the main diagonal (top-left to bottom-right)"""
    for i in range(0,3): # i : 0, 1, 2
        if  board[i][i] != player:
            return False
    return True
        
    # return all([board[i][i] == player for i in range(3)])

def check_diag2(player):
    """Checks if the player has won in the secondary diagonal (top-right to bottom-left)"""

    i = 0
    j = 2

    while i <= 2 and j >= 0:
        if board[i][j] != player :
            return False
        i += 1
        j -= 1
    return True
    
    # return all([board[i][2 - i] == player for i in range(3)])

def check_winner(player, row, col):
    """Checks if the current player has won the game"""
    return (check_row(player, row) or 
            check_col(player, col) or 
            check_diag1(player) or 
            check_diag2(player))

def is_valid_move(row, col):
    """Checks if the move is valid"""
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def play_game():
    player_turn = 'X'  # First player is 'X'
    moves_count = 0

    while True:
        print_board()
        # Input the move in the format "rowcol"
        move = input(f"Player {player_turn}, enter your move (e.g., 00 for top-left): ")
        row = int(move[0])
        col = int(move[1])
        if not is_valid_move(row, col):
            print("Invalid move! Try again.")
            continue
        
        # Update the board
        board[row][col] = player_turn
        moves_count  = moves_count + 1
        
        # After at least 5 moves, check for a winner
        if moves_count >= 5:
            if check_winner(player_turn, row, col):
                print(f"Player {player_turn} wins!")
                print_board()
                break

        # Check for a tie if the moves_count reaches 9
        if moves_count == 9:
            print("It's a tie!")
            print_board()
            break

        # Switch turns
        # player_turn = 'O' if player_turn == 'X' else 'X'
        if player_turn == 'X':
            player_turn = 'O'

        elif player_turn == 'O':
            player_turn = 'X'

if __name__ == "__main__":
    play_game()
