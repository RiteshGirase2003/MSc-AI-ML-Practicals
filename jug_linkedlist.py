class Node:
    def __init__ (self,prev,data,des):
        self.prev=prev
        self.data=data
        self.des = des



# Fill the jug based on index
def fill_jug(state, jug_index, capacities):
    state = list(state)
    # jug index : 0
    # [0, 0] -> list 
    # (4,3) -> capacity
    state[jug_index] = capacities[jug_index]  # Fill the specified jug
    # [4, 0]
    # (4, 0)
    return tuple(state)

# Empty the jug based on index
def empty_jug(state, jug_index):
    state = list(state)
    # [4,3]
    # index -> 0

    state[jug_index] = 0  # Empty the specified jug
    # [0, 3]
    # (0, 3)
    return tuple(state)

# Pour water from one jug to another
def pour_water(state, from_index, to_index, capacities):
    x, y = state

    # left side of min tells amount of water in donar jug
    # right tells that how much liters of space is empty in recieving jug
    transfer = min(state[from_index], capacities[to_index] - state[to_index])

    new_state = list(state)
    new_state[from_index] -= transfer
    new_state[to_index] += transfer
    return tuple(new_state)

# Action functions
def action_fill_jug1(state, capacities):
    return fill_jug(state, 0, capacities), "fill jug 1"  # Fill Jug 1

def action_fill_jug2(state, capacities):
    return fill_jug(state, 1, capacities), "fill jug 2"  # Fill Jug 2

def action_empty_jug1(state):
    return empty_jug(state, 0), " Empty jug 1"  # Empty Jug 1

def action_empty_jug2(state):
    return empty_jug(state, 1), "Empty jug 2"  # Empty Jug 2

def action_pour_jug1_to_jug2(state, capacities):
    return pour_water(state, 0, 1, capacities), " pour from jug 1 to jug 2"  # Pour Jug 1 to Jug 2

def action_pour_jug2_to_jug1(state, capacities):
    return pour_water(state, 1, 0, capacities) , " pour from jug 2 to jug 1 "  # Pour Jug 2 to Jug 1

# BFS function to solve the water jug problem using a list as a queue
def water_jug_bfs(capacities, goal, goal_jug,head):
    # Initial state: both jugs are empty
    initial_state = (0, 0)
    temp = head

    n = Node(temp,initial_state,"Initial state")
    temp = n
    # List to use as a queue for BFS
    queue = [initial_state]
    ll_queue = [temp]
    # Set to keep track of visited states
    visited = set()
    visited.add(initial_state)
    
    # Perform BFS
    while queue:
        current_state = queue.pop(0)  # Remove the first element from the list
        temp = ll_queue.pop(0)
        x, y = current_state

        print(f"Current state: Jug1 = {x} gallons, Jug2 = {y} gallons")

        # Check if we have reached the goal
        
        if current_state[goal_jug - 1] == goal:
            print("Goal reached!")
            return current_state,temp

        # List of possible actions
        actions = [
            action_fill_jug1,
            action_fill_jug2,
            action_empty_jug1,
            action_empty_jug2,
            action_pour_jug1_to_jug2,
            action_pour_jug2_to_jug1,
        ]

        # Try all possible actions
        for action in actions:
            if action in [action_fill_jug1, action_fill_jug2, action_pour_jug1_to_jug2, action_pour_jug2_to_jug1]:
                next_state,des = action(current_state, capacities)
            else:
                next_state,des = action(current_state)

            if next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)  # Add the new state to the end of the list
                n = Node(temp,next_state,des)
                ll_queue.append(n)

    print("Solution not found")
    return None

# User input for jug capacities and goal
jug1_capacity = int(input("Enter the capacity of Jug 1: "))
jug2_capacity = int(input("Enter the capacity of Jug 2: "))
goal = int(input("Enter the goal amount of water: "))
goal_jug = int(input("Which jug should hold the goal? (Enter 1 for Jug 1, 2 for Jug 2): "))

head = Node(None,(-1,-1),"dummy")
# Run the program to solve the water jug problem
state , temp_head = water_jug_bfs((jug1_capacity, jug2_capacity), goal, goal_jug,head)


temp = temp_head
s = []
d = {}
cnt = 0
while temp != None:
    s.append(cnt)
    d[cnt] = [temp.data,temp.des]
    cnt+=1

    temp = temp.prev

cnt = 1
for key in s[::-1]:
    lst = d[key]
    
    print(f"\n Step : {cnt} \n")
    print(f"  {lst[1]} -->  {lst[0]} ")
    cnt += 1