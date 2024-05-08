from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    maxSum = -float('inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            thisSum = node.val
            leftSum = max(dfs(node.left), 0)
            rightSum = max(dfs(node.right), 0)
            self.maxSum = max(self.maxSum, thisSum + leftSum + rightSum)
            thisSum += max(leftSum, rightSum)
            return thisSum

        dfs(root)
        return self.maxSum
