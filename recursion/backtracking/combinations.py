#https://leetcode.com/problems/combinations/submissions/
class Solution(object):
    def helper(self,main_list,combo_list,output,r,memo):
        #print main_list,combo_list
        #print combo_list,main_list
        if len(combo_list)==r:
            if tuple(sorted(combo_list)) not in memo:
                output.append(sorted(combo_list[:]))
                memo[tuple(sorted(combo_list))]=1
            return

        for i in range(len(main_list)):
            combo_list.append(main_list[i])
            self.helper(main_list[i+1:],combo_list,output,r,memo)
            combo_list.pop()

    def combine(self, n, r):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        main_list=range(1,n+1)
        #combo_list=[]
        output=[]
        memo={}
        self.helper(main_list,[],output,r,memo)
        return output



class Solution_leetcode:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first = 1, curr = []):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n + 1):
                # add i into the current combination
                curr.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        backtrack()
        return output




"""
1,2,3
    1, 2,3
        1,2, 3
        1,3  2
            1,2,3
            1,3,2
    2, 3
        2,3
    3


"""
