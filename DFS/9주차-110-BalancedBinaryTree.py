from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
## My Solution
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node, depth):
            if node is None:
                return depth
            left = check(node.left, depth+1)
            right = check(node.right, depth+1)
            if abs(left-right) > 1:
                return -1
            else:
                return max(left, right)
        
        rslt = check(root, 0)
        return rslt != -1
    

## Soluiton
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root):
            if root is None:
                return 0
            
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            return max(left, right)+1
        
        return check(root) != -1
