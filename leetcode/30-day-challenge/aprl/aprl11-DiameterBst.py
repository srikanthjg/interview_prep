"""
max depth:
with root,depth=1
if(root):
    -1
if(leafNode):
    return depth
max(leftsubtree(+1),rightsubtree(+1))


diameter:
longest edge distance

calc height of max(leftsubtree,rightsubtree) ==> for one node
call this for each subtree ==> diamter(leftsubtree,rightsubtree)

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.root = None
        self.max=0

    def insert(self,root,val):
        """
        if root == None:
            root = TreeNode(val)
            return

        #cur=root
        if (val<root.val):
            self.insert(root.left,val)
            print root.left.val ###NONE
        else:
            return self.insert(root.right,val)
        """
        if val == None:
            return root
        if root==None:
            root=TreeNode(val)
            return root

        if(val<root.val):
            root.left = self.insert(root.left,val)
        else:
            root.right = self.insert(root.right,val)

        return root

    def preorder(self,root):
        if(root):
            print root.val
            self.preorder(root.left)
            self.preorder(root.right)

    def max_depth(self,root,depth):

        ##-1 is important because depth +1 is passed
        if root == None:
            return depth-1

        ##leaf node
        if root.left == None and root.right==None:
            return depth

        return max(self.max_depth(root.left,depth+1),
            self.max_depth(root.right,depth+1))


    def diameterOfBinaryTree(self, root):
        if root==None:
            return 0
        return self.diameterOfBinaryTreeHelper(root)

    def diameterOfBinaryTreeHelper(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root==None:
            return self.max

        l = self.max_depth(root.left,1)
        r = self.max_depth(root.right,1)

        self.max= max(self.max,l+r)

        self.diameterOfBinaryTreeHelper(root.left)
        self.diameterOfBinaryTreeHelper(root.right)

        return self.max

sol=Solution()
root = TreeNode(20)

sol.insert(root,5)
sol.insert(root,6)
sol.insert(root,7)
sol.insert(root,8)
sol.insert(root,9)
sol.insert(root,10)

sol.insert(root,4)
sol.insert(root,3)
sol.insert(root,2)

sol.insert(root,25)
#sol.insert(root,23)
#sol.insert(root,26)
#sol.insert(root,27)

#sol.preorder(root)


print sol.diameterOfBinaryTree(root)
