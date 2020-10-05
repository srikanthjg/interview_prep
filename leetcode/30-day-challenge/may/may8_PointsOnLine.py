class Solution(object):
    def isPointOnLine(self,m,c,x,y):
        val=y-(m*x)-c
        if val==0:
            return True
        else:
            return False

    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates)==2:
            return True

        coordinates.sort()
        x1=coordinates[0][0]
        y1=coordinates[0][1]
        x2=coordinates[-1][0]
        y2=coordinates[-1][1]
        if x2-x1==0:
            m=float('inf')
        else:
            m=((y2-y1)//(x2-x1))
        c=y1-(m*x1)
        #print x1,y1,x2,y2
        #print m,c
        #print coordinates
        op=False
        for i in range(1,len(coordinates)-1):
            op=self.isPointOnLine(m,c,coordinates[i][0],coordinates[i][1])
            if op==False:
                return False
        return True


arr=[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
sol=Solution()
print sol.checkStraightLine(arr)
