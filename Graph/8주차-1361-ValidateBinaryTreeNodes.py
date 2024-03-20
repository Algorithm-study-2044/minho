from typing import List
import collections

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        #find the root
        visited = [0 for _ in range(n)]
        for i in range(n):
            if leftChild[i] != -1:
                if visited[leftChild[i]]:
                    return False
                visited[leftChild[i]] = 1
            if rightChild[i] != -1:
                if visited[rightChild[i]]:
                    return False
                visited[rightChild[i]] = 1
        try:
            root = visited.index(0)
        except: #there is no root
            return False
        #tree traversal
        path = [root]
        queue = collections.deque([root])
        while queue:
            i = queue.popleft()
            if leftChild[i] != -1:
                path.append(leftChild[i])
                queue.append(leftChild[i])
            if rightChild[i] != -1:
                path.append(rightChild[i])
                queue.append(rightChild[i])
        return len(path) == n  #if not, there is another tree
