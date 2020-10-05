#https://bradfieldcs.com/algos/graphs/prims-spanning-tree-algorithm/

from collections import defaultdict
import heapq
class Graph():
    def __init__(self,num_vertex=0):
        self.graph={}
        self.v=num_vertex
        self.distance={}


    def addEdge(self,edge):
        u,v,wt=edge
        if u not in self.graph:
            self.graph[u]=[]
        if v not in self.graph:
            self.graph[v]=[]
        self.graph[u].append((v,wt))
        return
    ### Check for vertex going to is visited or not
    ###
    def prim_spanning_tree(self,starting_vertex):
        mst = {}
        visited = set([starting_vertex])
        edges=[]
        for to, cost in self.graph[starting_vertex]:
            edges.append((cost,starting_vertex, to))
        heapq.heapify(edges)

        while edges:
            cost,u,v=heapq.heappop(edges)
            if v not in visited:
                visited.add(v)
                if u not in mst:
                    mst[u]=[]
                mst[u].append(v)
                #print "adding %r->%r"%(u,v)
                for u1,wt1 in self.graph[v]:
                    heapq.heappush(edges,(wt1,v,u1))
        return mst

sol=Graph(6)
edges=[('A','B',10),('A','C',8),('B','E',6),('E','A',1)]
#map(sol.addEdge,edges)
for e in edges:
    sol.addEdge(e)
print sol.graph
print sol.prim_spanning_tree('A')
