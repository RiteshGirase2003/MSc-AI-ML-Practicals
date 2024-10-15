# The A* (A-star) algorithm is a pathfinding and graph traversal algorithm
#  used to find the shortest path between two points
# A* evaluates the cost of each step in terms of:

# g(n):  actual cost travel till now.
# h(n): The heuristic estimate of the cost to get from current to goal.
# f(n) = g(n) + h(n)

# Heuristic: A function that estimates how close a node (current position) is to the goal
# It provides a guess that helps the algorithm make smarter decisions.




    

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

def find_in_goal(goal_state, element):
    for i in range(len(goal_state)):
        for j in range(len(goal_state[i])):
            if goal_state[i][j] == element:
                return i, j



# Function to calculate the Manhattan distance heuristic
# Manhattan Distance= ∣x1−x2∣+∣y1−y2∣
# x1 , y1 current coordinates of the tile.
# x2, y2  target coordinates of the tile.

def manhattan_distance(board, goal):
    distance = 0
    for i in range(len(board)): # travel number of rows
        for j in range(len(board[i])): # travel number of columns 
            
            if board[i][j] != 0:  # Skip the empty tile
                element = board[i][j] # this stores element present at position i, j

                x_goal, y_goal = find_in_goal(goal,element) # it finds position element in goal state
                
                # ∣ x1 − x2 ∣ + ∣ y1 − y2 ∣
                # x1 = i , y1 = j
                # x2 = x_goal , y2 = y_goal
                # abs means absolute value ( it ignores sign of ingeter and makes it positive )
                # for example : 1 - 10 => -9 and 10 - 1 => 9 but by putting it in abs it always positive value ie 9

                distance = distance + abs(i - x_goal) + abs(j - y_goal)
    return distance

# Check if current state is the goal state
def is_goal(board, goal):
    return board == goal

# Function to generate all possible next states by sliding the blank space
def get_state(board):
    state_lst = []
    x, y = find_zero(board) # finds position of 0
    n = len(board) # number of rows
    
    # Define moves for   up, down, left, right
    
    moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

    # let's assume that 0 is at 1,1
    # [ (0,1), (2,0), (1,0), (1,2)]
    
    for i, j in moves:
        if 0 <= i < n and 0 <= j < n: # for checking boundar
            # Create a new board by swapping tiles

            # # Copy the current board
            new_board =[]
            for row in board:
                new_board.append(row[::])

            new_board[x][y], new_board[i][j] = new_board[i][j], new_board[x][y]
            state_lst.append(new_board)
    
    return state_lst

# Function to calculate the total cost (f = g + h)
def total_cost(state, g, goal_state):
    h = manhattan_distance(state, goal_state)
    result = g + h 
    return result

# Function to create a sorting key for open_set
def f(value):
    board_state, g = value
    val = total_cost(board_state, g, goal_state)
    return val
# Function to solve the puzzle using A* algorithm
def solve_puzzle(initial_state, goal_state):
    # Create a queue for states to explore, starting with the initial state
    open_set = [(initial_state, 0)]  # (board, moves so far ie g)
    visited = []  # List to track visited states

    while open_set:
        # Sort by total cost (g + h) using the sort_key function
        open_set.sort(key=f)
        current, moves = open_set.pop(0)

        if is_goal(current, goal_state):
            print("Goal state reached in", moves, "moves:")
            print_board(current)
            return
        
        # Skip already visited states
        if current in visited:
            continue

        # Mark current state as visited
        visited.append(current)

        print(moves)
        print_board(current)

        # Get the neighbors (possible next states) and add them to the open set
        state_lst = get_state(current)
        for state in state_lst:
            if state not in visited:
                open_set.append((state, moves + 1))

    print("No solution found.")

# Initial and goal states
initial_state = [[2, 8, 3], 
                 [1, 6, 4], 
                 [7, 0, 5]]

goal_state = [[1, 2, 3], 
              [8, 0, 4], 
              [7, 6, 5]]

# Solve the puzzle
print("Initial state:")
# print_board(initial_state)
solve_puzzle(initial_state, goal_state)
