class  Node(object):
    def __init__(self, arg):
        self.val = arg
        self.right = None
        self.left = None

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

    def createNode(self,arr):
        if arr[0] == 'X':
            node = None
            arr.pop(0)
            return node

        node = Node(arr[0])
        arr.pop(0)
        node.left = self.createNode(arr)
        node.right= self.createNode(arr)
        return node

    def deserialize(self,arr):
        return self.createNode(arr)



#[2,1,3]
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
bst.root = bst.deserialize(bst.arr)
bst.printT(bst.root)
