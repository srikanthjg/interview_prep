class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # (key):refcount,index

        hashmap={}
        index=0
        for i in s:
            if i not in hashmap:
                hashmap[i]=[1,index]
            else:
                hashmap[i]=[hashmap[i][0]+1,index]

            index=index+1

        #print hashmap
        minIndex=len(s)

        for val in hashmap.values():
            if val[0] ==1:
                if val[1]<minIndex:
                    minIndex=val[1]
        if minIndex==len(s):
            return -1
        else:
            return minIndex
