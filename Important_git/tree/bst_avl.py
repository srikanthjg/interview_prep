class Node(object):
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None
        self.height=0



class Bst(object):
    def __init__(self):
        self.root = None

    def get_height(self,root):
        if root==None:
            return 0
        return root.height

    def insert_avl(self,root,val):

        #Insert BST
        if root==None:
            return Node(root)
        #print root.val
        if val<root.val:
            root.left = self.insert_rec(root.left, val)
        if val>root.val:
            root.right = self.insert_rec(root.right, val)

        root.height=self.get_height(root)
        #balance factor
        bf = self.get_height(root.left)-self.get_height(root.right)

        ##left
        #linked list of left (left heavy)
        if bf>1 and val<root.left.val:
            #self.right_rotate(root)
            print "left"

        #left right
        if bf>1 and val>root.left.val:
            #root.left=self.left_rotate(root.left)
            #self.right_rotate(root)
            print "left right"

        #right
        if bf<-1 and val>root.right:
            print "left rotate"

        #left right
        if bf<-1 and val<root.right:
            print "left right"

        return root

    def get_height(self,root):
        if root==None:
            return 0

        return 1+max(self.get_height(root.left),self.get_height(root.right))
