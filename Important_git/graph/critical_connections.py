class Solution(object):
    def __init__(self,num_vertex=0):
        self.graph={}
        #self.inverse_graph={}
        self.num_vertex=num_vertex
        self.output=[]
        #self.visited={}
        #self.stack=[]

    def addEdge(self,edge):
        u,v=edge

        if u not in self.graph:
            self.graph[u]=[]
        if v not in self.graph:
            self.graph[v]=[]

        self.graph[u].append(v)
        self.graph[v].append(u)

        return

    def dfs1(self,root,visited):
        visited[root]=True
        neigh=self.graph[root]
        for u in neigh:
            if u not in visited:
                self.dfs1(u,visited)

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

        adj=self.graph[v]
        i=0
        for i in range(len(adj)):
            if u==adj[i]:
                break
        if len(self.graph[v])!=0:
            self.graph[v].pop(i)

    def srikagov(self,n,out):

        list_nodes=range(n)
        #print list_nodes
        visited_edges={}
        for v in self.graph.keys():
            for u in self.graph[v]:
                #remove one edge u,v in graph
                #u,v=1,2
                if u==v or (u,v) in visited_edges:
                    continue
                    #pass
                self.delEdge(u,v)
                visited_edges[(u,v)]=1
                visited_edges[(v,u)]=1
                visited={}
                self.dfs1(u,visited)
                if len(visited)!=(n):
                    out.append([u,v])
                self.addEdge((u,v))

        return




    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        map(self.addEdge,connections)
        self.num_vertex=len(self.graph.keys())
        out=[]
        self.srikagov(n,out)
        #out.sort(key=lambda x:x[0])
        #print out
        return out

        #remove edge and do dfs on one of verticies, check if all are visited, else add to output
        
