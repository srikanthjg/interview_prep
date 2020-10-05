# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self,root,parent,depth,target):
        if root==None:
            return -1,-1
        if root.val==target:
            return parent.val,depth

        lp,ld=self.dfs(root.left,root,depth+1,target)
        rp,rd=self.dfs(root.right,root,depth+1,target)

        if ld==-1 and rd==-1:
            return -1,-1
        if ld==-1 and rd!=-1:
            return rp,rd
        if ld!=-1 and rd==-1:
            return lp,ld

        return

    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if root ==None:
            return None
        depth=0
        lp,ld=self.dfs(root,root,depth+1,x)
        rp,rd=self.dfs(root,root,depth+1,y)

        print lp,ld,rp,rd
        if lp!=rp and ld==rd:
            return True
        else:
            return False
