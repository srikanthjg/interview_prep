class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        sq={}
        i=1
        while(i*i<=num):
           sq[i*i]=1
           i=i+1
        if num in sq:
            return True
        else:
            return False
