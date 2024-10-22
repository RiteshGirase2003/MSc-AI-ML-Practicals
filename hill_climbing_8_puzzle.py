import random
import copy

# Function to print the puzzle board
def print_board(board):
    for row in board:
        print(row)
    print()

# Function to find the (x, y) position of the empty space (0)
def find_zero(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j

# Function to find the (x, y) position of an element in the goal state
def find_in_goal(goal_state, element):
    for i in range(len(goal_state)):
        for j in range(len(goal_state[i])):
            if goal_state[i][j] == element:
                return i, j

# Manhattan distance heuristic
def manhattan_distance(board, goal):
    distance = 0
    for i in range(len(board)):  # travel number of rows
        for j in range(len(board[i])):  # travel number of columns
            if board[i][j] != 0:  # Skip the empty tile
                element = board[i][j]  # this stores element present at position i, j
                x_goal, y_goal = find_in_goal(goal, element)  # Find position in goal state
                distance += abs(i - x_goal) + abs(j - y_goal)  # Calculate Manhattan distance
    return distance

# Check if current state is the goal state
def is_goal(board, goal):
    return board == goal

# Generate all possible next states by sliding the blank space
def get_state(board):
    state_lst = []
    x, y = find_zero(board)  # Find position of 0
    n = len(board)  # number of rows
    
    # Define moves for up, down, left, right
    moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    
    for i, j in moves:
        if 0 <= i < n and 0 <= j < n:  # Check boundaries
            # Copy the current board and swap tiles
            new_board = copy.deepcopy(board)
            new_board[x][y], new_board[i][j] = new_board[i][j], new_board[x][y]
            state_lst.append(new_board)
    
    return state_lst

# Hill climbing algorithm for 8-puzzle problem
def hill_climbing_puzzle(initial_state, goal_state):
    current_state = initial_state
    current_h = manhattan_distance(current_state, goal_state)
    iterations = 0
    
    while True:
        print(f"Iteration {iterations}:")
        print_board(current_state)
        
        # Get neighbors and evaluate their heuristic
        neighbors = get_state(current_state)
        next_state = None
        next_h = current_h
        
        for neighbor in neighbors:
            h = manhattan_distance(neighbor, goal_state)
            if h < next_h:  # We want to minimize the Manhattan distance
                next_h = h
                next_state = neighbor
        
        # If no better neighbor is found, we are stuck in a local optimum
        if next_state is None or next_h >= current_h:
            print("Reached a local maximum or goal.")
            break
        
        # Move to the neighbor with the best (lowest) heuristic
        current_state = next_state
        current_h = next_h
        iterations += 1
        
        # If the goal state is reached, stop
        if is_goal(current_state, goal_state):
            print("Goal state reached:")
            print_board(current_state)
            break

    return current_state, current_h

# Initial and goal states
initial_state = [[2, 8, 3], 
                 [1, 6, 4], 
                 [7, 0, 5]]

goal_state = [[1, 2, 3], 
              [8, 0, 4], 
              [7, 6, 5]]

# Solve the puzzle using Hill Climbing
print("Initial State:")
print_board(initial_state)

final_state, final_h = hill_climbing_puzzle(initial_state, goal_state)
print("Final Manhattan distance:", final_h)
