class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            mergedNode = TreeNode(root1.val + root2.val)
            mergedNode.left = self.mergeTrees(root1.left, root2.left)
            mergedNode.right = self.mergeTrees(root1.right, root2.right)
        elif root1:
            return root1
        elif root2:
            return root2
        else:
            return None
        
        return mergedNode
