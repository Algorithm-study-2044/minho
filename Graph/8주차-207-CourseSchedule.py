from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)

        finished = [0 for _ in range(numCourses)]

        def check(course, path):
            if finished[course]:
                return True
            if course in path:
                return False
            for j in graph[course]:
                if not finished[j]:
                    if check(j, path+[course]) == False:
                        return False
            finished[course] = 1
            return True
        
        for i in range(numCourses):
            if check(i, []) == False:
                return False
        return True
