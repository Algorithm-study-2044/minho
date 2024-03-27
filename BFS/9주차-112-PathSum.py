from typing import Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
## 1. BFS
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        queue = collections.deque([(root, root.val)])
        while queue:
            node, psum = queue.popleft()    # path sum
            if (node.left or node.right) is None:
                if psum == targetSum:
                    return True
                else:
                    continue
            if node.left:
                queue.append((node.left, psum + node.left.val))
            if node.right:
                queue.append((node.right, psum + node.right.val))

        return False
    
## 2. DFS
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        def dfs(node, psum):
            if (node.left or node.right) is None:
                return psum == targetSum
            if node.left:
                if dfs(node.left, psum+node.left.val) == True:
                    return True
            if node.right:
                if dfs(node.right, psum+node.right.val) == True:
                    return True
            return False

        return dfs(root, root.val)
