"""
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319/

1>find MBS set - int(log(n,2))
2>xor with all 1 with be the complement


"""

import math
class Solution(object):
    def findMsbSetBit(self,num):

        i=32
        val=1<<i

        while(i>=0):
            op=val&num
            if op:
                return i
            i=i-1
            val=val>>1

        return -1


    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num==0:
            return 1

        #indexSet= self.findMsbSetBit(num)
       # if index ==-1:
       #     return 1
        indexSet=int(math.log(num,2)) #################

        val=(1<<(indexSet+1))-1
        print indexSet,val,(indexSet+1)
        return val^num
