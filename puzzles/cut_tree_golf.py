class Solution(object):
    count=0
    def getNeigh(self,node,forest,visited):
        x,y=node
        neigh=[]
        dir=[(1,0),(-1,0),(0,-1),(0,1)]
        for dx,dy in dir:
            newx=dx+x
            newy=dy+y
            if 0<=newx<len(forest) \
                and 0<=newy<len(forest[0]):
                    #print newx,newy
                    if (newx,newy) not in visited \
                    and forest[newx][newy]!=0 \
                    and forest[newx][newy]>forest[x][y]:
                        neigh.append((newx,newy))
        return neigh


    def dfs(self,node,visited,forest,ground_map):

        if node in visited:
            return


        visited[node]=1
        del ground_map[node]
        neigh=self.getNeigh(node,forest,visited)
        self.count+=1
        for x,y in neigh:
            if (x,y) not in visited:
                self.dfs((x,y),visited,forest,ground_map)



    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """

        ground_map={}
        visited={}
        #count=0
        if forest[0][0]==0:
            return 0

        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j]>=1:
                    ground_map[(i,j)]=1

        root=(0,0)

        self.dfs(root,visited,forest,ground_map)


        if len(ground_map)==0:
            return -1
        return count
