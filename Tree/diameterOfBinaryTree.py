class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return 0 
            return 1 + max(helper(root.left), helper(root.right)) 
        
        if not root: 
            return 0
        
        return max(helper(root.right) + helper(root.left), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
