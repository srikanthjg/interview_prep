
##Preorder
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root==None:
            return "X"

        return str(root.val)+","+self.serialize(root.left)+","+self.serialize(root.right)

    def deserialize_helper(self,arr):
        if len(arr)==0:
            return None
        node_val=arr.pop(0)
        if node_val=='X':
            return None
        node=TreeNode(node_val)
        node.left=self.deserialize_helper(arr)
        node.right=self.deserialize_helper(arr)
        return node

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        #print data
        arr=data.split(",")
        #print arr
        return self.deserialize_helper(arr)
