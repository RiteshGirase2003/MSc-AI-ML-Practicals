# Python program that demonstrates the hill climbing algorithm to find the maximum of a mathematical function.
# For example f(x) = -x^2 + 4x


# Local Search
# Greedy Algo - jo bhi best lage ko karna ( universally best hoga don't know )
# No backtrack 

# Basic Rule ->  If new state is better then current state then it is our new current state


#  Algorithm
# 1. Evaluate initial state ( randomly kuch value lo )
# 2. Loop until solution is found or thier is no operations left
    # i. select and apply a new operation
    # ii. Evaluate new state ( if it is goal then quit ) 
    # loop it until we get better state then our current state or we have not reached our goal state.

# Problems in Hill climbing 
# i. Local Minima -> means it is not overall highest peak ( may be it can happend that thier exist a global maxima means highest peak over all)
# ii. Flat Plateu / Flat maximum -> Here all neighbors having same values ( means in tree all childs are of same huriestic value )
# iii. Ridge -> it is trapasium like hill but one side is at high and other is low 

# Use case
# 


import random

# Define the mathematical function
def f(x):
    return -x**2 + 4*x

# Hill Climbing algorithm
def hill_climbing(start, step_size, max_iterations):
    current_x = start
    current_value = f(current_x)
    
    for i in range(max_iterations):
        # Explore the neighbors
        next_left = current_x - step_size # current state - step size ( 0.1 )
        next_right = current_x + step_size
        
        next_value_left = f(next_left) # current state - step size ( 0.1 )
        next_value_right = f(next_right) # current state + step size ( 0.1 )
        flag = True
        # Check which direction gives a better value
        if next_value_left > current_value: # if left side give better value then current state 
            # then new state becomes our current state
            current_x = next_left
            current_value = next_value_left
            flag = False
        if next_value_right > current_value: # if right side gives better value then current state 
            # then new state becomes our current state 
            current_x = next_right
            current_value = next_value_right
            flag = False

        if flag:
            # If neither neighbor improves, we've reached a peak
            print(f"Local maximum found after {i+1} iterations.")
            break
            
    return current_x, current_value

# Main function to test the hill climbing algorithm
if __name__ == "__main__":
    # Starting point
    start = random.uniform(0, 4)  # Random starting point between 0 and 4 ( any number between num >= 0 and num < 4) uniform means each number has equal chance of getting selected
    #  start value will be in between 0 and 4

    step_size = 0.01  # Small step size to explore neighbors
    max_iterations = 1000  # Maximum number of iterations
    
    max_x, max_value = hill_climbing(start, step_size, max_iterations)
    print(f"Maximum found at x = {max_x}, f(x) = {max_value}")
