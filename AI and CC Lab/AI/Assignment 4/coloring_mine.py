def colorGraph(graph, n):
    result = {}
    for u in range(n):
        print("Vertex: ", u)
        assigned = set(result[i] for i in graph[u] if i in result)
        print("Assigned :", assigned)
        
        color = 1
        while color < n:
            if color not in assigned:
                break
            color +=1
        result[u] = color

    for v in range(n):
            print("Vertex :", v, "Color:->", result[v])
# graph = {0:[1,2,3], 1:[0,2], 2:[0,1,4], 3:[0],4:[2]}
graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2],
}
colorGraph(graph, 3)