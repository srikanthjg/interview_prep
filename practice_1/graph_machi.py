
class Graph:


    def __init__(self):
        self.graph = {}

    def addEdge(self, e):
        u, v = e

        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)

        return True

    def DFS(self, root):

        visited = {}

        self.DFSHelper(visited, root)

    def DFSHelper(self, visited, root):
        if root in visited:
            return

        for v in self.graph[root]:
            self.DFSHelper(visited, v)

        visited[root] = True
        print root



g = Graph()
edges = [('A','J'), ('A','G'), ('A','B'), ('A','C'), ('B','H'), ('B','I')]
for e in edges:
    g.addEdge(e)

g.DFS('A')
