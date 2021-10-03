#https://bradfieldcs.com/algos/graphs/prims-spanning-tree-algorithm/
"""
Greedy
similar to djikstra , Uses min heap.
Prim does not use relax nodes. That is only for distances


ALGO:
While T is not yet a spanning tree
   Find an edge that is safe and smallest to add to the tree
   Add the new edge to T


Time Complexity: O(ElogV)
"""
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
        visited = set(starting_vertex)
        edges=[]
        #Build edges with min heap for starting vertex
        for to, cost in self.graph[starting_vertex]:
            heapq.heappush(edges,(cost,starting_vertex, to)) #==> heapify based on cost (x[0])
        #heapq.heapify(edges)

        while edges:
            cost,frm,to=heapq.heappop(edges)
            if to not in visited:
                visited.add(to)
                mst[frm]=(to,cost)
                for to_nxt,wt in self.graph[to]:
                    heapq.heappush(edges,(wt,to,to_nxt))
        return mst

sol=Graph(6)
edges=[('A','B',4),('A','H',8),('D','E',6)]
map(sol.addEdge,edges)
print sol.graph
print sol.prim_spanning_tree('A')
