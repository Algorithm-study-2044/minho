from typing import List
import sys, collections, heapq

class Solution:
    ans = sys.maxsize
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flights.sort(key=lambda x: x[2])
        graph = collections.defaultdict(list)
        for f, t, p in flights:
            graph[f].append((t, p))
        visited = [0] * n
        visited[src] = 1
        def dfs(city, price, k):
            if city == dst:
                self.ans = min(self.ans, price)
                return
            if k < 0:
                return
            if price > self.ans:
                return
            
            for t, p in graph[city]:
                if not visited[t]:
                    visited[t] = 1
                    dfs(t, price+p, k-1)
                    visited[t] = 0
            return 
        
        dfs(src, 0, k)
        return self.ans if self.ans != sys.maxsize else -1
    ## Time Limit Exceeded
    # 다익스트라 알고리즘 사용해야

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for f, t, p in flights:
            graph[f].append((t, p))
        
        heap = [(0, src, 0)]    # (price, city, stops)
        while heap:
            price, city, stops = heapq.heappop(heap)
            if city == dst:
                return price
            if stops > k:
                continue
            for t, p in graph[city]:
                heapq.heappush(heap, (price+p, t, stops+1))

        return -1
    ## Time Limit Exceeded -> 최소힙 알고리즘

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for f, t, p in flights:
            graph[f].append((t, p))
        
        output = [float('inf') for _ in range(n)]
        output[src] = 0
        
        queue = collections.deque([(src, 0, 0)])   # (city, price, step)
        while queue:
            city, price, step = queue.popleft()
            if step > k:
                continue
            for t, p in graph[city]:
                if price+p < output[t]:
                    output[t] = price + p
                    queue.append((t, price+p, step+1))
        
        return output[dst] if output[dst] != float('inf') else -1 
    # solution - queue 이용
