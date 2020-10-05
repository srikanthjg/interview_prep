"""

bellman_ford is used to find negative cycles NOT positive cycles!!!!!!!
So it cant be used to find cycle in a graph generically

"""

class Graph():
    def __init__(self,num_vertex=0):
        self.graph={}
        self.num_vertex=num_vertex
        self.distance={}


    def addEdge(self,edge):
        u,v,wt=edge
        if u not in self.graph:
            self.graph[u]=[]
        if v not in self.graph:
            self.graph[v]=[]
        self.graph[u].append((v,wt))
        return

    def bellman_ford(self,s,edges):
        for i in self.graph.keys():
            self.distance[i]=float('inf')
        #print "root=%r"%s
        self.distance[s]=0
        #for all edges=V-1
        """
        edge_list=[]
        #create edge list
        for vertex,val in self.graph.items():
            for u,wt in val:
                edge_list.append((vertex,u,wt))
        """
        #print edges
        #all vertex - root = V-1
        #edge = v->u
        for i in range(self.num_vertex-1):
            for cur,nxt,wt in edges:
                if self.distance[nxt]>self.distance[cur]+wt:
                    self.distance[nxt]=self.distance[cur]+wt

        #is NEGATIVE cycle
        for cur,nxt,wt in edges:
            if self.distance[nxt]>self.distance[cur]+wt:
                print "Negative Cycle in Graph!!!"
                return False

        print self.distance
        return True


sol=Graph(3)
#Change -4 to 4, negative cycle wont be formed and bellman_ford will pass
edges=[('A','B',1),('B','C',2),('C','A',-4)]
map(sol.addEdge,edges)
print sol.graph
print sol.bellman_ford('A',edges)
