class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones.sort()
        #print stones
        if len(stones)==1:
            return stones[0]
        if len(stones)==0:
            return 0

        x=stones[-1]
        y=stones[-2]
        if x==y:
            stones.pop(-1)
            stones.pop(-1)
        else:
            stones[-2] = abs(y-x)
            stones.pop(-1)

        #print stones
        return self.lastStoneWeight(stones)



sol=Solution()
stones=[2,7,4,1,8,1]
sol.lastStoneWeight(stones)
