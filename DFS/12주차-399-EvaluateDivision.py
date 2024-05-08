from typing import List
import collections

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        answer = []
        graph = collections.defaultdict(list)
        for i, equations in enumerate(equations):
            graph[equations[0]].append((equations[1], values[i]))
            graph[equations[1]].append((equations[0], 1/values[i]))
        print(graph)
    
        def dfs(node, target):
            if node in visited:
                return -1
            visited.add(node)

            for adj, value in graph[node]:
                if adj == target:
                    return value
                out = dfs(adj, target)
                if out != -1:
                    return value * out
            
            return -1

        for query in queries:
            visited = set()
            answer.append(round(dfs(query[0], query[1]), 5))

        return answer
