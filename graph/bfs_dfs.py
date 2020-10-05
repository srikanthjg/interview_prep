
class Graph(object):
    def __init__(self,numVertices=0):
        self.graph_dict = {}
        for i in range(numVertices):
            self.graph_dict[i]=[]

    def addEdge(self,edge):
        v1 = edge[0]
        v2 = edge[1]
        self.graph_dict[v1].append(v2)

    def dfs_util(self,v,visited):
        visited[v] = True
        #print "vertex = %d"%v

        adj_list = self.graph_dict[v]

        #for all adj ,
        for adj in adj_list:
            if(visited[adj]!=True):
                self.dfs_util(adj,visited)

    def dfs(self,root):
        #num_vertex = len(self.graph_dict.keys())
        #key = vertex , value = bool
        visited = {}

        for i in self.graph_dict.keys():
            visited[i] = False

        self.dfs_util(root,visited)


    def bfs(self,root):
        num_vertex = len(self.graph_dict.keys())
        #key = vertex , value = bool
        visited = {}

        for i in self.graph_dict.keys():
            visited[i] = False

        q = []
        q.append(root)

        while(q):
            vertex = q.pop(0)
            visited[vertex] = True
            #print vertex, visited[vertex]
            for v in self.graph_dict[vertex]:
                #print v,visited[v]
                if(visited[v] == False):
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
