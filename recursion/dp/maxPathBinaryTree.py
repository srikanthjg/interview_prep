"""
https://www.youtube.com/watch?v=_wUz0XKQ5JM
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/532/week-5/3314/
max path should include node.

   10
9       20
      15   7
max path = 9,10,20,15

if root=-10
max path = 20,15,7

Algorithm:

maximum="-inf"
l=left subtree (here i have to return max(left/right subtree) +node.
r=right subtree
(cant return the same max at the node because i shouldnt
include the subtree again-only max of left/right subtree)

max at a node = max(max,l+r+val)
"""


class Solution(object):
    def __init__(self):
        self.maximum=float("-inf")

    def dfs(self,root):
        if root==None:
            return 0
        l=self.dfs(root.left)
        r=self.dfs(root.right)
        self.maximum = max(self.maximum,l+r+root.val)  # ==> is NOT returned
        return max(l,r) +root.val  # ==> return only max left/right subtree

    def maxPathSum(self,root):
        self.dfs(root)
        return self.maximum
