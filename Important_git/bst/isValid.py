# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def helper(self,root):
        if not root:
            return True,float('inf'),float('-inf')

        l,lmin,lmax=self.helper(root.left)
        r,rmin,rmax=self.helper(root.right)
        #print root.val,l,lmin,lmax,r,rmin,rmax
        if l==False or r==False:
            return False,0,0

        if lmax>=root.val or rmin<=root.val:
            return False,0,0

        return True,min(root.val,lmin,rmin),max(root.val,lmax,rmax)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root: return True

        b,v1,v2= self.helper(root)
        return b
