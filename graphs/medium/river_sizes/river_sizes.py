# Time: O(wh) | Space: O(wh)
def river_sizes(matrix):
    rivers = []
    visited = [[False for col in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverse_node(i, j, matrix, visted, rivers)
    return rivers

def traverse_node(i, j, matrix, visited, rivers):
    curr_river_size = 0
    nodes_to_explore =[[i, j]]
    while len(nodes_to_explore):
        curr_node = nodes_to_explore.pop()
        i = curr_node[0]
        j = curr_node[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        curr_river_size += 1
        unvisited_neighbors = get_unvisited_neighbors(i, j, matrix, visited)
        for neighbor in unvisited_neighbors:
            nodes_to_explore.append(neighbor)
    if curr_river_size > 0:
        rivers.append(curr_river_size)
        
def get_unvisited_neighbors(i, j, matrix, visited):
    unvisited_neighbors = []
    if i > 0 and not visited[i-1][j]:
        unvisited_neighbors.append(matrix[i-1][j])
    if j > 0 and not visited[i][j-1]:
        unvisited_neighbors.append(matrix[i][j-1])
    if i < len(matrix) and not visited[i+1][j]:
        unvisited_neighbors.append(matrix[i+1][j])
    if j > len(matrix[0]) and not visited[i][j+1]:
        unvisited_neighbors.append(matrix[i][j+1])
    return unvisited_neighbors
