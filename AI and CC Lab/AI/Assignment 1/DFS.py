import collections
visited = set()

def bfs(graph, root):
    visited = set()
    queue = collections.deque([root])
    while queue:
        vertex = queue.popleft()
        visited.add(vertex)
        for i in graph[root]:
            if i not in visited:
                queue.append(i)
    print("bfs is ", visited)
    print(queue)

def dfs(graph, root):
    if root not in visited:
        ans.append(root)
        visited.add(root)
        for neighbour in graph[root]:
            dfs(graph, neighbour)


ans = []
graph = {0:[1, 2,3], 1:[0,2], 2:[0,1,4], 3:[0],4:[2]}
bfs(graph, 0)
dfs(graph, 0)
print("dfs is",ans)
