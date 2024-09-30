# DFS -> Depth First Search
# used for searching and travelling/traversal on Graphs ( Trees )
# Data structure used -> Stack
# stack works on LIFO 


# What is dictionary
# Key Value pair

# Dictionary is represented using  {}
# { key : value }
# { key1 : value1, key2 : value2}

# To access the value of a dictionary Dict_name[key]

graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4, 5],
    4: [2, 3, 5],
    5: [3, 4]
}

visited = []  # Keep track of visited nodes
stack = [1]  # Start with node 1

while len(stack) > 0:
    element = stack.pop()  # Get the last element (LIFO)

    if element not in visited:  # Check if the node has not been visited
        visited.append(element)  # Mark the node as visited
        print(element, end=" -> ") #  Print the element

        # Push all the adjacent nodes onto the stack
        for i in graph[element]:
            if i not in visited and i not in stack:  # Only add 'un-visited nodes' /'nodes not in stack'  to the stack
                stack.append(i)
