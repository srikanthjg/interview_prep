# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    s=0
    def countUnivalSubtrees_h(self,root):

        if root == None:
            return False,-999
        print root.val

        #leaf node
        if root.left==None and root.right==None:
            #self.s=self.s+1
            return True,root.val

        l,ret = self.countUnivalSubtrees_h(root.left)
        r,ret = self.countUnivalSubtrees_h(root.right)
        if root.left and root.right:
            f = (l and r) and (root.val==retl) and (root.val==retr)
        if root.left and root.right==None:
            f = l and (root.val==retl)
        if root.left== None and root.right:
            f = r and (root.val==retr)
        if f:
            self.s=self.s+1

        return f,root.val

    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.countUnivalSubtrees_h(root)
        return self.s
