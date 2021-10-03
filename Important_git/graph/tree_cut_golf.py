import heapq
class Solution(object):

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
                    and forest[newx][newy]!=0:
                        neigh.append((newx,newy))
        return neigh

    def bfs(self,forest,src,dst):
        level=0
        q=[(level,src)]
        visited=set()
        visited.add(src)

        while q:
            level,src=q.pop(0)
            r,c=src
            if src==dst:
                return level
            #for node in self.getNeigh(src,forest,visited):
            for node in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                x,y=node
                if 0<=x<len(forest) \
                    and 0<=y<len(forest[0]):
                    if forest[x][y]!=0 and node not in visited:
                        visited.add(src)
                        q.append((level+1,node))
        return -1

    def bfs1(self,forest,src,dst ):
        sr, sc=src
        tr, tc=dst
        R, C = len(forest), len(forest[0])
        queue = collections.deque([(sr, sc, 0)])
        seen = {(sr, sc)}
        while queue:
            r, c, d = queue.popleft()
            if r == tr and c == tc:
                return d
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if (0 <= nr < R and 0 <= nc < C and
                        (nr, nc) not in seen and forest[nr][nc]):
                    seen.add((nr, nc))
                    queue.append((nr, nc, d+1))
        return -1

    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        #heap of heights
        trees=[]
        #map of ground and trees
        #ground_map={}
        if forest[0][0]==0:
            return -1


        for i in range(len(forest)):
            for j in range(len(forest[0])):
                #if forest[i][j]>=1:
                    #ground_map[(i,j)]=forest[i][j]
                if forest[i][j]>1:
                    heapq.heappush(trees,(forest[i][j],(i,j)))

        src=(0,0)
        #print self.getNeigh(root,forest,visited)
        walk=0
        while len(trees):
            dst_height,dst=heapq.heappop(trees)
            d=self.bfs1(forest,src,dst)
            if d==-1:
                return -1
            #print d
            walk+=d
            src=dst

        return walk
