graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4, 5],
    4: [2, 3, 5],
    5: [3, 4]
}

graph = {
    'A' : ['B', 'C', 'D'],
    'B':[],
    'C':['E','F'],
    'D':[],
    'E':[],
    'F':[]
}
visited = []
queue = ['A']

while len(queue) > 0:
    element = queue.pop(0)
    print(element, end=" -> ")
    visited.append(element)
    for i in graph[element]:
        if i not in visited and i not in queue: 
            queue.append(i)
    