
class Node(object):
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None
        self.x = 0
        self.y = 0


class Bst(object):
    def __init__(self):
        self.root = None
        self.ht = {}

    def insert_rec(self,root,val):

        if root==None:
            root=Node(val)
            #print root.val
            return root
        #print root.val
        if val<root.val:
            root.left = self.insert_rec(root.left, val)
        if val>root.val:
            root.right = self.insert_rec(root.right, val)
        return root

    def insert(self,val):
        if(self.root==None):
            self.root=Node(val)
            return

        cur = self.root
        while(cur):
            if val<cur.val:
                if cur.left == None:
                    cur.left = Node(val)
                    return
                cur = cur.left
            if val> cur.val:
                if cur.right == None:
                    cur.right = Node(val)
                    return
                cur = cur.right
        return

    def trasform_mirror(self,root):
        if(root == None):
            return

        root.left,root.right = root.right,root.left
        self.trasform_mirror(root.left)
        self.trasform_mirror(root.right)

    def compare_mirror(self,root1,root2):
        if root1==None and root2!=None:
            return False
        if root1!=None and root2==None:
            return False

        if root1==None and root2==None:
            return True

        if root1.val != root2.val:
            return False

        return self.compare_mirror(root1.left,root2.right) and self.compare_mirror(root1.right,root2.left)

    max_depth = 0
    def max_depth(self,root,depth):
        if root == None:
            return depth-1 ##==>  to offset depth+1 that is being passed

        #leaf node
        if root.right == None and root.left == None:
            return depth

        max_depth = max(self.max_depth(root.left,depth+1),self.max_depth(root.right,depth+1))
        return max_depth



    # Compute the "maxDepth" of a tree -- the number of nodes
    # along the longest path from the root node down to the
    # farthest leaf node
    def maxDepth(node):
        if node is None:
            return 0

        else:

            # Compute the depth of each subtree
            lDepth = maxDepth(node.left)
            rDepth = maxDepth(node.right)

            # Use the larger one
            if (lDepth > rDepth):
                return lDepth+1
            else:
                return rDepth+1

    def minDepth(root):
        # Corner Case.Should never be hit unless the code is
        # called on root = NULL
        if root is None:
            return 0

        # Base Case : Leaf node.This acoounts for height = 1
        if root.left is None and root.right is None:
            return 1

        # If left subtree is Null, recur for right subtree
        if root.left is None:
            return minDepth(root.right)+1

        # If right subtree is Null , recur for left subtree
        if root.right is None:
            return minDepth(root.left) +1

        return min(minDepth(root.left), minDepth(root.right))+1


    min_depth = 0
    def min_depth(self,root,depth):
        if root == None:
            return depth-1

        if root.right == None and root.left == None:
            return depth
##handle 2 - 1child case:
        if root.left == None:
            return self.min_depth(root.right,depth+1)
        if root.right == None:
            return self.min_depth(root.left,depth+1)

        return min(self.min_depth(root.left,depth+1),self.min_depth(root.right,depth+1))


    def preorder(self,root):
        if root == None:
            return
        print "%d"%root.val
        self.preorder(root.left)
        self.preorder(root.right)

    def preorder_c(self,root):
        if root == None:
            return
        print "val=%d,x=%d,y=%d"%(root.val,root.x,root.y)
        self.preorder_c(root.left)
        self.preorder_c(root.right)

    def preorder_itr(self,root):
        stack=[]
        cur=root
        while(1):
            while(cur):
                print cur.val
                stack.append(cur)
                cur=cur.left
            if not stack:
                break
            cur=stack.pop()
            cur=cur.right

    def bfs(self,root):
        if root==None:
            return

        q=[]
        q.append(root)
        cur=root
        while(q):
            #next_level = []
            size=len(q)
            for i in range(size):
                cur = q.pop(0)
                print cur.val
                if cur.left:
                    #next_level.append(node.left)
                    q.append(cur.left)
                if cur.right:
                    #next_level.append(node.right)
                    q.append(cur.right)
                #this_level = next_level

        return

    def search(self,root,target):
        if root == None:
            return False
        if root.val == target:
            return True
        return self.search(root.right,target) or self.search(root.left,target)

    def inorder_travesal(self,root,node,target):
        if node == None:
            return False

        if self.search(root,abs(node.val-target)):
            return True
        return self.inorder_travesal(root,node.right,target) or self.inorder_travesal(root,node.left,target)

    def zigzag_traversal(self,root):
        pass


    def two_sum(self,root,target):
        #for every node in bst, find target-root.val
        return self.inorder_travesal(root,root,target)


##############  Vertical BST Print ##############
    def vertical_bst_print_populate(self,root,x):
        if root==None:
            return

        if x not in self.ht:
            self.ht[x]=[]
        self.ht[x].append(root.val)
        self.vertical_bst_print_populate(root.right,x+1)
        self.vertical_bst_print_populate(root.left,x-1)

    def vertical_bst_print(self,root):
        for ele in sorted(self.ht.keys()):
            print self.ht[ele]

#############################################

##############  Path Sum Print ##############
    pathSum=[]
    def path_sum3_h(self,root,sum,target,path):
        if root==None:
            return

        val=sum+root.val
        if val>target:
            return

        path.append(root.val)
        #print "path=%r,sum=%r,val=%r,target=%r"%(path,sum,val,target)
        if val==target:
            self.pathSum.append(path)
            return
        self.path_sum3_h(root.right,val,target,path)
        self.path_sum3_h(root.left,val,target,path)

    def path_sum3(self,root,target):
        if root == None:
            return []

        self.path_sum3_h(root,0,target,[])
        self.path_sum3(root.right,target)
        self.path_sum3(root.left,target)

########################################################

bst = Bst()
bst.root = bst.insert_rec(bst.root, 10)
bst.insert_rec(bst.root, 5)
bst.insert_rec(bst.root, 15)
bst.insert_rec(bst.root, 20)
bst.insert_rec(bst.root, 12)
bst.insert_rec(bst.root, 6)
bst.insert_rec(bst.root, 2)


## Traversal
bst.bfs(bst.root)
#bst.preorder_itr(bst.root)
print ""
#bst.preorder(bst.root)


#bst.vertical_bst_print_populate(bst.root,0,0)
#bst.vertical_bst_print(bst.root)
#bst.path_sum3(bst.root, 6)
#print bst.pathSum


#bst.inorder(bst.root)
#print ""
#bst.trasform_mirror(bst.root)
#bst.preorder_c(bst.root)
print ""

#print bst.max_depth(bst.root,0)
#print bst.min_depth(bst.root,1)


#print bst.two_sum(bst.root,18)


"""
bst2=Bst()
bst2.insert(10)
bst2.insert(5)
bst2.insert(15)
bst2.insert(3)
bst2.insert(2)
bst2.inorder(bst2.root)
print bst2.compare_mirror(bst.root,bst2.root)
"""
