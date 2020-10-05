import heapq
class Graph():
    def __init__(self,num_vertex=0):
        self.graph={}
        self.v=num_vertex


    def addEdge(self,edge):
        u,v,wt=edge
        if u not in self.graph:
            self.graph[u]=[]
        if v not in self.graph:
            self.graph[v]=[]
        self.graph[u].append((v,wt))
        return


    def djikstra(self,root):
        distance={}
        for v in self.graph.keys():
            distance[v]=float('inf')
        q=[]
        distance[root]=0

        heapq.heappush(q,(0,root))
        print q,distance
        while q:
            #extract min
            prev_distance,node=heapq.heappop(q)
            for v,wt in self.graph[node]:

                #relax
                if distance[v]>prev_distance+wt:
                    distance[v]=prev_distance+wt
                heapq.heappush(q, (distance[v],v))
        return distance

sol=Graph(6)
edges=[('A','B',4),('B','E',1),('A','D',3),('D','E',6)]
map(sol.addEdge,edges)
print sol.graph
print sol.djikstra('A')
