class Solution1(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    dia=0
    memo={}
    dia_memo = {}
    def depth(self,root):
        if root in self.memo:
            return self.memo[root]

        if root ==None:
            self.memo[root]=0
            return 0

        self.memo[root]= 1+max(self.depth(root.right),self.depth(root.left))
        return self.memo[root]

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return self.dia

        if root in self.dia_memo:
            return self.dia_memo[root]

        l=self.depth(root.left)
        r=self.depth(root.right)

        dia_sum=l+r
        self.dia_memo[root]=dia_sum

        if self.dia<dia_sum:
            self.dia=dia_sum

        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)

        return self.dia
