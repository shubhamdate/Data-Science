class Graph:

    def __init__(self, vertices, edges, parent):
        self.vertices = vertices
        self.edges = edges
        self.parent = parent

    def find(self, x):
        if self.parent[x] < 0:
            return x
        return self.find(self.parent[x])

    def kruskal(self):
        self.edges = sorted(self.edges, key=lambda item: item[2])
        result = []
        e = 0

        for i in range(len(self.edges)):

            start, end, weight = self.edges[i]
            parentX, parentY = self.find(start), self.find(end)

            if parentX != parentY:
                result.append(self.edges[i])

                self.parent[parentX] = parentY
                e += 1
            if e == vertices-1:
                return result
        return False


if __name__ == '__main__':
    # edges = [(0, 1, 4), (0, 2, 4), (1, 2, 2), (1, 0, 4), (2, 0, 4), (2, 1, 2), (2, 3, 3),
    #          (2, 5, 2), (2, 4, 4), (3, 2, 3), (3, 4, 3), (4, 2, 4), (4, 3, 3), (5, 2, 2), (5, 4, 3)]

    edges = [(1, 0, 2), (0, 2, 3), (2, 3, 4), (1, 3, 15), (1, 2, 1)]

    # vertices = 6
    vertices = 4
    parent = [-1 for _ in range(vertices)]

    g = Graph(vertices, edges, parent)
    ans = g.kruskal()
    print(ans)

# Time complexity: O(ElogV+ElogE)
