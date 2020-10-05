class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        Smap={}

        for s in S:
            if s not in Smap:
                Smap[s]=1
            else:
                Smap[s]=Smap[s]+1

        count=0
        print Smap
        for j in J:
            if j in Smap:
                if Smap[j]==0:
                    continue
                else:
                    count=count+Smap[j]
        return count
