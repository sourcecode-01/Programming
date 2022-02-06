class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rst = []
        if root:
            rst.extend(self.postorderTraversal(root.left))
            rst.extend(self.postorderTraversal(root.right))
            rst.append(root.val)
        return rst
      

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]
        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
                stack.append(root.left)
                stack.append(root.right)
        return res[::-1]
