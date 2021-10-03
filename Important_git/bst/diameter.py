def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

                result=0

                def diameter(root=root):
                     nonlocal result
                     if not root:
                        return 0

                     left=diameter(root.left)
                     right=diameter(root.right)

                     result=max(result,left+right)

                     return 1+max(left,right)

                diameter()
                return result   
