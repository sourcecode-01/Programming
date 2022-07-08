def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        if root:
            q.append(root)
        res = []
        
        while q:
            val = []
            for i in range(len(q)):
                node = q.popleft()
                val.append(node.val)
            
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        
            res.append(val)
        return res
