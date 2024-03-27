from typing import List
import collections

## 1. Topological Sort
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)

        in_degree = [0 for _ in range(numCourses)]
        for i in range(numCourses):
            for j in graph[i]:
                in_degree[j] += 1

        queue = collections.deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        rslt = []
        while queue:
            i = queue.popleft()
            for j in graph[i]:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    queue.append(j)
            rslt.append(i)
        
        return rslt if len(rslt) == numCourses else []
    
## 2. DFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)

        finished = [0 for _ in range(numCourses)]
        rslt = []

        def check(course, path):
            if finished[course]:
                return True
            for j in graph[course]:
                if not finished[j]:
                    if j in path or check(j, path+[course]) == False:
                        return False
            finished[course] = 1
            rslt.append(course)
            return True

        for i in range(numCourses):
            if check(i, []) == False:
                return []
        return rslt
    

## 3. Final
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        inbound = [0 for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)
            inbound[a] += 1

        queue = collections.deque()
        for i in range(numCourses):
            if inbound[i] == 0:
                queue.append(i)
        
        rslt = []
        while queue:
            i = queue.popleft()
            for j in graph[i]:
                inbound[j] -= 1
                if inbound[j] == 0:
                    queue.append(j)
            rslt.append(i)
        
        return rslt if len(rslt) == numCourses else []
