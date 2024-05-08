from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_cost = [float('inf')] * len(points)
        visited = [False] * len(points)
        min_cost[0], visited[0] = 0, True
        heap = [(0, 0)]

        while heap:
            _, i = heapq.heappop(heap)
            visited[i] = True
            for j in range(len(points)):
                if visited[j]:
                    continue
                cost = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                if cost < min_cost[j]:
                    min_cost[j] = cost
                    heapq.heappush(heap, (cost, j))

        return sum(min_cost)
    

#2 visited 최적화
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_cost = [float('inf')] * len(points)
        unvisited = set([i for i in range(len(points))])

        min_cost[0] = 0
        heap = [(0, 0)]
        while heap:
            _, i = heapq.heappop(heap)
            if i in unvisited:
                unvisited.remove(i)
            for j in unvisited:
                cost = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                if cost < min_cost[j]:
                    min_cost[j] = cost
                    heapq.heappush(heap, (cost, j))

        return sum(min_cost)
