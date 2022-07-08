# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        q = collections.deque([root])
        
        while q:
            rightSide = None
            
            for i in range(len(q)):
                node = q.popleft()
                
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    rightSide = node
            if rightSide:
                res.append(rightSide.val)
        return res
