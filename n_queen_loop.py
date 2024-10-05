def is_safe(board, row, col):
    # Vertical Check
    for i in range(len(board)):
        if i >= row:
            break
        if board[i][col] == 1:
            return False
        
    # Upper Left Check
    i = row - 1
    j = col - 1 
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Upper Right Check
    i =  row - 1
    j =  col + 1

    while i >= 0 and j <= 3:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1  

    return True  # It's safe to place the queen here


def solve_queens(n):
    # Initialize the board as a 2D array of size n x n filled with 0 (no queens placed)
    # board = [ [ -1, -1, -1,-1], [ -1, -1, -1, -1 ], [ -1, -1, -1, -1 ], [ -1, -1, -1, -1 ] ]
    board = []
    for _ in range(n):
        l = [-1]*n
        board.append(l)

        


    row = 0  # Start with the first row
    col = 0  # Start at the first column

    while row >= 0:
        placed = False  # Indicates if a queen was placed in the current row

        # Try to place the queen in the next available column
        while col < n:
            if is_safe(board, row, col):
                # Place the queen (mark with a 1)
                board[row][col] = 1
                placed = True
                col = 0  # Reset column to start from the first in the next row
                break  # Move to the next row
            col += 1  # Move to the next column in the current row

        print_solution(board)


        if placed:
            # If we successfully placed a queen in the last row, we found a solution
            if row == n - 1:
                print("Solution:")
                print_solution(board)
                break
                

        if placed:
            # Move to the next row to place the next queen
            row += 1
        else:
            # If no queen was placed in the current row, backtrack
            row -= 1
            # Find the column of the last placed queen and move to the next column
            if row >= 0:
                col = board[row].index(1) + 1  # Find where the queen was and move to the next column
                board[row][col-1] = 0  # Remove the queen

    


def print_solution(board):
    # Print the current configuration of the board
    print("--------------------")

    for i in board:
        for j in i:
            if j == 1:
                print('Q',end=' ')
            else:
                print('_',end=' ')
        print()

    print("--------------------\n\n")


# Test the function with 4 queens
solve_queens(4)
