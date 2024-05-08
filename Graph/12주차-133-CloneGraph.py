# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        
# fail
from typing import Optional
class Solution:
    visited = set()
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None or node.val in self.visited:
            return []
        new = Node(node.val, node.neighbors)
        self.visited.add(new.val)
        for adj in new.neighbors:
            self.cloneGraph(adj)
        return new
    
## Solution
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return node
        copied = {}
        
        def dfs(node):
            if node in copied:
                return copied[node]
            new = Node(node.val)
            copied[node] = new
            for neighbor in node.neighbors:
                new.neighbors.append(dfs(neighbor))
            return new
        
        return dfs(node)
