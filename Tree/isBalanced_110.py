def height(root):
        if root is None:
            return 0
        return max(height(root.left), height(root.right)) + 1
    
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
 
        lh = height(root.left)
        rh = height(root.right)
 
        if (abs(lh - rh) <= 1) and self.isBalanced(
        root.left) is True and self.isBalanced( root.right) is True:
            return True

        return False
