class Solution(object):

    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        a={}
        for i in range(0,32,2):
            tmp=1<<(i)
            a[tmp]=0

        if num in a:
            return True

        return False
