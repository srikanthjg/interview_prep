
class Node(object):
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

class Bst(object):
    def __init__(self):
        self.depth=0

#### TOP Down
    def maxDepth_td(self,root,depth):
        if root == None:
            return 0
        if root.left == None and root.right==None:
            self.depth=max(depth+1,self.depth)
            return self.depth
        self.maxDepth_td(root.right,depth+1)
        self.maxDepth_td(root.left,depth+1)

### Bottom UP
    def maxDepth_bu(self,root):
        if root == None:
            return 0
        l=self.maxDepth_bu(root.left)
        r=self.maxDepth_bu(root.right)
        return max(l,r)+1
