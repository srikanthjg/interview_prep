class Solution(object):
    def countEle2(self,arr):

        ## Set doesnt support indexing
        s=list(set(arr))
        if len(s)==1:
            return 0
        count=0
        for i in range(1,len(s)):
            if(s[i]-s[i-1]==1):
                count=count+1
        return count

    def countEle(self,arr):
        hmap={}
        for i in arr:
            if(i not in hmap):
                hmap[i] = 1
            else:
                hmap[i] = hmap[i]+1
        count=0
        key=hmap.keys()
        for i in range(1,len(key)):
            if(key[i]-key[i-1]==1):
                count=count+hmap[key[i-1]]
        #print count
        return count

arr=[1,3,2,3,5,0]
sol=Solution()
#print sol.isBitSet(1,1)
print sol.countEle(arr)
