
class Graph():
    def __init__(self,num_vertex=0):
        self.graph={}
        self.inverse_graph={}
        self.v=num_vertex
        self.output=[]
        self.visited={}
        self.stack=[]

    def addEdge(self,edge):
        u,v=edge

        if u not in self.graph:
            self.graph[u]=[]
        if v not in self.graph:
            self.graph[v]=[]

        if u not in self.inverse_graph:
            self.inverse_graph[u]=[]
        if v not in self.inverse_graph:
            self.inverse_graph[v]=[]

        self.graph[u].append(v)
        self.inverse_graph[v].append(u)
        self.visited[u]=False
        self.visited[v]=False
        return

    def dfs1(self,root):
        self.visited[root]=True
        neigh=self.graph[root]
        for u in neigh:
            if self.visited[u]==False:
                self.dfs1(u)
                self.stack.append(u)

    def dfs2(self,root,new_set):
        self.visited[root]=True
        new_set.append(root)
        neigh=self.graph[root]
        for u in neigh:
            if self.visited[u]==False:
                self.dfs2(u,new_set)
        return


    def getUnvisited(self,all_visited_flag):
        for u in self.visited.keys():
            if self.visited[u]==False:
                all_visited_flag=False
                return u

        all_visited_flag=True
        return None


    def scc_kosa_raju(self):
        #dfs on graph
        #1st pass
        all_visited_flag=False
        for v in self.graph.keys():
            if self.visited[v]==False:
                self.stack.append(v)
                self.dfs1(v)

        #dfs on inverted graph
        #2nd pass
        del self.visited
        self.visited={}
        for u in self.inverse_graph.keys():
            self.visited[u]=False
        print "inverse_graph=%r"%self.inverse_graph
        print "stack=%r"%self.stack
        while self.stack:
            root=self.stack.pop()
            new_set=[]
            if self.visited[root]==False:
                self.dfs2(root,new_set)
                self.output.append(new_set)
        return self.output

sol=Graph(6)
edges=[('A','B'),('B','C'),('C','A'),('A','E')]
map(sol.addEdge,edges)
print "graph=%r"%sol.graph
print sol.scc_kosa_raju()
