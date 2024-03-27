import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

## 1. My solution
class Solution:
    LCA = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, p, q):
            if node is None:
                return node
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)
            if node.val == p.val or node.val == q.val:
                if left or right:
                    self.LCA = node
                return node
            elif left and right:
                self.LCA = node
                return node
            return left or right
        
        dfs(root, p, q)
        return self.LCA
    

## 2. Solution
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root:
            if root == p or root == q:
                return root
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)

            if left and right:
                return root
            elif left:
                return left
            else:
                return right

## Lowest Common Ancestor Algo
    # 1) 모든 노드의 깊이를 계산
    # 2) 최소 공통 조상을 찾을 두 노드를 확인
        # (1) 먼저 두 노드의 깊이가 동일하도록 거슬러 올라간 뒤
        # (2) 부모가 같아질 때까지 반복하여 거슬러 올라감
