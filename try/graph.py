class Graph(object):
    def __init__(self):
        #self.root=None
        self.graph_adj={}
        self.size=0

    def addEdge(self,edge):
        v0=edge[0]
        v1=edge[1]

        if v0 not in self.graph_adj:
            self.graph_adj[v0]=[v1]
        else:
            self.graph_adj[v0].append(v1)

        if v1 not in self.graph_adj:
            self.graph_adj[v1]=[v0]
        else:
            self.graph_adj[v1].append(v0)

        self.size += 1

    def dfs_util(self,v,visited):
        visited[v] = True
        print v
        for adj in self.graph_adj[v]:
            if visited[adj]!=True:
                self.dfs_util(adj,visited)

    def dfs(self,v):
        visited={}
        for adj in self.graph_adj.keys():
            visited[adj]=False

        self.dfs_util(v,visited)

    def bfs(self,v):
        visited={}
        for adj in self.graph_adj.keys():
            visited[adj]=False

        q=[]
        q.append(v)
        while(q):
            print q
            node = q.pop(0)
            visited[node]=True
            print node
            for adj in self.graph_adj[node]:
                if visited[adj]==False:
                    q.append(adj)




arr1 = [[10,5],[5,4],[4,3],[10,15],[15,14],[15,30]]

g = Graph()
for arr in arr1:
    g.addEdge(arr)
print "adj list of graph = %r"%g.graph_adj

#root = 10
print "dfs"
print g.dfs(10)
print "bfs"
print g.bfs(10)
