
"""

Time Complexity: O(V+E)  ==> mainly DFS
"""

class Solution(object):

    topo_sort_result=[]
    def topo_sort_helper(self,g,v,visited,path):
        #print v
        if v in path:
            #Cycle found
            #print "cycle found"
            return True

        path[v]=True
        for u in g[v]:
            if u not in visited:
                cycle=self.topo_sort_helper(g,u,visited,path)
                if cycle:
                    return True
        self.topo_sort_result.insert(0,v)
        del path[v]
        visited[v]=True

        return False

    def topo_sort(self,g):
        visited={}
        path={}
        # this loop is for all the individual roots==>ingress=0
        #Will work for diconnected graphs also
        for v in g.keys():
            if v not in visited:
                t=self.topo_sort_helper(g,v,visited,path) ##DFS
                if t==True:
                    return True
        return False


    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        g={}


        # Create a Directed Graph
        for v in range(numCourses):
            g[v]=[]
        for u,v in prerequisites:
            g[u].append(v)

        t=self.topo_sort(g)
        #print self.topo_sort_result,t
        return not t
