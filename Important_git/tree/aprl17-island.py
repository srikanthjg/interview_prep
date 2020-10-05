class Solution(object):
    def dfs(self,root,grid,not_visited):
        #print root
        i,j=root
        #left,rigth,up,down
        dir=[(-1,0),(1,0),(0,1),(0,-1)]

        neigh=self.getNeigh(grid,root,not_visited)
        for newx,newy in neigh:
            del not_visited[(newx,newy)]
            self.dfs((newx,newy),grid,not_visited)

    def getNeigh(self,grid,node,not_visited):
        i,j=node
        dir=[(-1,0),(1,0),(0,1),(0,-1)]
        neigh=[]
        for x,y in dir:
            newx=x+i
            newy=y+j
            if 0<=newx<=len(grid)-1 and 0<=newy<=len(grid[0])-1\
            and (newx,newy) in not_visited:
                if grid[newx][newy]=="1":
                    neigh.append((newx,newy))
        return neigh

    def bfs(self,root,grid,not_visited):
        i,j=root
        #left,rigth,up,down
        q=[root]

        while q:
            node=q.pop(0)
            if node in not_visited:
            #print not_visited
                del not_visited[node]
            else:
                continue
            adj=self.getNeigh(grid,node,not_visited)
            for x,y in adj:
                if (x,y) in not_visited:
                    q.append((x,y))

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid)==0:
            return 0

        not_visited={}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    not_visited[(i,j)]=1
        count=0
        print not_visited
        while 1:
            keys_arr=not_visited.keys()
            if len(keys_arr)==0:
                break

            #pick a root
            root=keys_arr[0]
            #del not_visited[root]
            #print root,keys_arr
            self.bfs(root,grid,not_visited)
            count+=1
        return count

sol=Solution()
grid=[['1','1','0','0','0'],['1','0','0','1','1']]
print sol.numIslands(grid)
