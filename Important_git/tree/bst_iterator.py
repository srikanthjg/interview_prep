# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack=[]
        self.cur=root
        self.val=None
        #leftmost
        while self.cur:
            self.stack.append(self.cur)
            self.cur=self.cur.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """


        node=self.stack.pop()
        self.val=node.val
        #print self.val
        if node.right:
            self.cur=node.right
            #if self.cur!=None:
            while self.cur:
                self.stack.append(self.cur)
                self.cur=self.cur.left
        return self.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """

        if len(self.stack)==0:
            return False


        return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
"""
["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]
[[[7,3,15,null,null,9,20]],[null],[null],[null],[null],[null],[null],[null],[null],[null]]
"""
