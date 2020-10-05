class  Node(object):
    def __init__(self, arg):
        self.val = arg
        self.right = None
        self.left = None

######WRONG!!!!!!!!!!!


class Bst(object):
    def __init__(self):
        self.root = None
        self.arr = []

    def printT(self,node):
        if(node == None):
            return
        print node.val
        self.printT(node.left)
        self.printT(node.right)

    def serialize(self,node):
        if node == None:
            self.arr.append('X')
            return
        self.arr.append(node.val)
        self.serialize(node.left)
        self.serialize(node.right)
        return

    def createNode(self,i,node):
        if i == len(self.arr)-1:
            return

        if self.arr[i] == 'X':
            node = None
            return

        node = Node(self.arr[i])
        self.createNode(i+1,node.left)
        self.createNode(i+1,node.right)

    def deserialize(self,node):
        self.createNode(0,node)
        return



bst = Bst()
bst.root = Node(10)
bst.root.left = Node(5)
bst.root.left.left = Node(3)
bst.root.right = Node(15)
bst.root.right.right = Node(17)
bst.root.right.left = Node(13)
#print
bst.printT(bst.root)


bst.serialize(bst.root)
print bst.arr
bst.deserialize(bst.root)
bst.printT(bst.root)
