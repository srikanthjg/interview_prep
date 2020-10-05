# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def dfs(self,root,p,paths):
        if root == None:
            return paths
        p=p+str(root.val)
        if root.left==None and root.right==None:
            paths.append(p)

        if root.left!=None:
            self.dfs(root.left,p+"->",paths)
        if root.right!=None:
            self.dfs(root.right,p+"->",paths)


    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths=[]


        self.dfs(root,"",paths)
        return paths
