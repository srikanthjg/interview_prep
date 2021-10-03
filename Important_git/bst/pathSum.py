#https://leetcode.com/problems/path-sum-iii/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathFromRoot(self,root,target):
        if not root:
            return 0
        l=self.pathFromRoot(root.left,target-root.val)
        r=self.pathFromRoot(root.right,target-root.val)
        if root.val==target:
            return 1+l+r
        return l+r

    def h(self,root,target):
        if not root:
            return 0

        p=self.pathFromRoot(root,target)
        l=self.h(root.left,target)
        r=self.h(root.right,target)
        #print root.val,p,l,r
        return p+l+r

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        return self.h(root,sum)



###### My Solution ############


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathFromRoot(self,root,target,cur_sum,count):
        if not root:
            return

        cur_sum+=root.val
        if cur_sum==target:
            count[0]+=1

        self.pathFromRoot(root.left,target,cur_sum,count)
        self.pathFromRoot(root.right,target,cur_sum,count)

        return

    def h(self,root,target,count):
        if not root:
            return


        self.pathFromRoot(root,target,0,count)
        self.h(root.left,target,count)
        self.h(root.right,target,count)
        return

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        count=[0]
        self.h(root,sum,count)
        return count[0]
