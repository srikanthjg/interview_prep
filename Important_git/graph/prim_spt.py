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

    def prim_spanning_tree(self,starting_vertex):
        mst = {}
        visited = set([starting_vertex])
        for to, cost in self.graph[starting_vertex]:
            edges = [(starting_vertex, to,cost)]
        heapq.heapify(edges)

        while edges:
            frm,to,cost=heapq.heappop(edges)
            if to not in visited:
                visited.add(to)
                mst[frm]=to
                for u,wt in self.graph[to]:
                    heapq.heappush(edges,(frm,u,wt))
        return mst

sol=Graph(6)
edges=[('A','B',4),('A','H',8),('D','E',6)]
map(sol.addEdge,edges)
print sol.graph
print sol.prim_spanning_tree('A')
