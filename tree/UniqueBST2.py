#https://leetcode.com/problems/unique-binary-search-trees-ii/


# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

import itertools
class Solution(object):
    def insertBst(self,node,val):
        if node==None:
            return TreeNode(val)
        if val<node.val:
            node.left=self.insertBst(node.left,val)
        elif val>node.val:
            node.right=self.insertBst(node.right,val)
        return node

    def level_order(self,root,bst):
        if root==None:
            return
        q=[root]
        while q:
            level=[]
            for i in range(len(q)):
                cur=q.pop(0)
                if cur.left:
                    q.append(cur.left)
                    level.append(cur.val)
                else:
                    level.append('X')
                if cur.right:
                    q.append(cur.right)
                    level.append(cur.val)
                else:
                    level.append('X')
            bst.append(level)



        return

    def generateTrees(self, n):

        """
        :type n: int
        :rtype: List[TreeNode]
        """

        p=list(itertools.permutations(range(1,n+1)))
        print p
        out=[]
        for node_list in p:
            root=TreeNode(node_list[0])
            for node_val in node_list[1:]:
                self.insertBst(root,node_val)
            bst=[]
            self.level_order(root,bst)
            out.append(bst)
        return out

sol=Solution()
print sol.generateTrees(3)

root=TreeNode(2)
sol.insertBst(root, 3)

bst=[]
sol.level_order(root,bst)
print bst
