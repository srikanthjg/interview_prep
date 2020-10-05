"""
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3305/
Return the root node of a binary search tree that matches the
given preorder traversal.

(Recall that a binary search tree is a binary tree where
for every node, any descendant of node.left has a value < node.val,
and any descendant of node.right has a value > node.val.
Also recall that a preorder traversal displays the value of
the node first, then traverses node.left, then traverses node.right.)

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):

    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        i=0
        root=TreeNode(preorder[0])
        for i in range(1,len(preorder)):
            self.insert(root,preorder[i])
        return root

    def insert(self,root,val):
        if root==None:
            root=TreeNode(val)
            return root
        if val<root.val:
            root.left =  self.insert(root.left,val)
        if val>root.val:
            root.right = self.insert(root.right,val)
        return root

    arr=[]
    def preorder(self,root):
        if root:
            print root.val
            self.arr.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

sol=Solution()
root=TreeNode(10)
sol.insert(root,5)
sol.insert(root,3)
sol.insert(root,15)
sol.insert(root,17)
sol.insert(root,13)
sol.preorder(root)
print sol.arr

sol.preorder(sol.bstFromPreorder(sol.arr))
