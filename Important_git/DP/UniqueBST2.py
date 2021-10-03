#https://leetcode.com/problems/unique-binary-search-trees-ii/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import itertools
class Solution(object):

    def getTree(self,start,end):
        if start>end:
            return [None]

        if start==end:
            return [TreeNode(start)]

        all_tree=[]
        #pick a root
        for i in range(start,end+1):
            l_tree=self.getTree(start,i-1)
            r_tree=self.getTree(i+1,end)
            #connect root to all possible combos of l and r
            for l in l_tree:
                for r in r_tree:
                    cur_tree=TreeNode(i)
                    cur_tree.left=l
                    cur_tree.right=r
                    all_tree.append(cur_tree)
        return all_tree


    def generateTrees(self, n):

        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0:
            return []
        return   self.getTree(1,n)
