class Solution(object):
    visited={}
    def dfs(self,x,y,val,image):
        maxX=len(image)-1
        maxY=len(image[0])-1
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        self.visited[x,y]=1
        for dir in directions:
            newx=x+dir[0]
            newy=y+dir[1]
            if 0<=newx<=maxX and 0<=newy<=maxY:
                if image[newx][newy]==val:
                    if (newx,newy) not in self.visited:
                        self.dfs(newx,newy,val,image)

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.visited.clear()
        self.dfs(sr,sc,image[sr][sc],image)
        #print self.visited

        for k,v in self.visited.items():
            x=k[0]
            y=k[1]
            image[x][y]=newColor
            #self.visited.pop(k)
        #print image

        return image
