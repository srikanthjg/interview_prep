import copy
class Solution(object):

    def combine(self, arr):
        tmp=[]
        tmp = copy.copy(arr)
        for x in tmp:
            arr.append(x^1)
        return arr

    def kthGrammar_h(self,N,K,i,arr):
        if i == N:
            return \
            self.combine(arr)

        print arr
        arr = self.combine(arr)
        return self.kthGrammar_h(N,K,i+1,arr)

    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N==1:
            return 0

        arr = self.kthGrammar_h(N,K,1,[0])
        print arr
        return arr[K-1]

sol = Solution()
print sol.kthGrammar(3, 1)
