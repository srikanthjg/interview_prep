class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap={}
        for x in nums:
            if x not in hashmap:
                hashmap[x]=1
            else:
                hashmap[x]=hashmap[x]+1

        print hashmap
        maximumRefcount=-float('inf')
        maxKey=-1
        for k,v in hashmap.items():
            if v>=maximumRefcount:
                maximumRefcount=v
                maxKey = k

        return maxKey
