class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        op=m
        ## can be optimized further for checking same till 2^20
        #2^31
        if n>1073741824 and m<=1073741824:
            op=m
            m=1073741824
        while(m!=n+1):
            op=op&m
            if op==0:
                return op

            m=m+1
        #print op
        return op
