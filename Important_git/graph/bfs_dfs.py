"""
BFS
T: O(V+E)
S: O(V)

DFS
T: O(V+E)
S: O(V)

"""


class Graph(object):
    def __init__(self,numVertices=0):
        self.graph_dict = {}
        for i in range(numVertices):
            self.graph_dict[i]=[]

    def addEdge(self,edge):
        v1 = edge[0]
        v2 = edge[1]
        self.graph_dict[v1].append(v2)

    def delEdge(self,u,v):
        if u==v:
            return

        adj=self.graph[u]
        i=0
        for i in range(len(adj)):
            if v==adj[i]:
                break
        if len(self.graph[u])!=0:
            self.graph[u].pop(i)
        """
        #for undirected Graph
        adj=self.graph[v]
        i=0
        for i in range(len(adj)):
            if u==adj[i]:
                break
        if len(self.graph[v])!=0:
            self.graph[v].pop(i)
        """

    def dfs_util(self,v,visited):
        visited[v] = True
        print "vertex = %d"%v

        #for all adj ,
        for adj in self.graph_dict[v]:
            if(adj not in visited):
                self.dfs_util(adj,visited)

    def dfs(self,root):
        #num_vertex = len(self.graph_dict.keys())
        #key = vertex , value = bool
        visited = {}
        self.dfs_util(root,visited)


    def bfs(self,root):
        num_vertex = len(self.graph_dict.keys())
        #key = vertex , value = bool
        visited = {}

        q = []
        q.append(root)

        while(q):
            vertex = q.pop(0)
            visited[vertex] = True
            #print vertex, visited[vertex]
            for v in self.graph_dict[vertex]:
                if v not in visited:
                    q.append(v)

arr1 = [[1,2],[4,5],[1,4],[2,5]]

g = Graph(6)
for edge in arr1:
    g.addEdge(edge)
print "adj list of graph = %r"%g.graph_dict

#root = 10
print "dfs"
print g.dfs(1)
print "bfs"
print g.bfs(1)
