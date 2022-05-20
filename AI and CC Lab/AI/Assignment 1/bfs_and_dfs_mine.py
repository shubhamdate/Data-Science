#Implementing BFS
import collections
def bfs(graph, root):
    visited = set()
    queue = collections.deque([root])

    while queue:
        vertex = queue.popleft()
        visited.add(vertex)
        for i in graph[vertex]:
            if i not in visited:
                queue.append(i)
    print("BFS using Queue is: ", visited)



if __name__== "__main__":
    #Dictionary
    graph = {0:[1, 2,3], 1:[0,2], 2:[0,1,4], 3:[0],4:[2]}
    bfs(graph,0)



#  recursive approch for DFS
visited = set()
def dfs(graph, root):

    if root not in visited:
        ans.append(root)
        visited.add(root)
        for neighbour in graph[root]:
            dfs(graph, neighbour)
    #print(visited)


ans = []
graph = {0:[1, 2,3], 1:[0,2], 2:[0,1,4], 3:[0],4:[2]}
dfs(graph, 0)
print("DFS Solution using recursive Approch :", ans)