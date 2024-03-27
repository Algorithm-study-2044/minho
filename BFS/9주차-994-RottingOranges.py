from typing import List
import collections

## 1.
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dr, dc = [1, -1, 0, 0], [0, 0, -1, 1]

        queue = collections.deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))

        time = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for i in range(4):
                    nr, nc = r+dr[i], c+dc[i]
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
            time += 1

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return -1
        return time-1 if time else 0

## 2. 알고리즘 개선
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dr, dc = [1, -1, 0, 0], [0, 0, -1, 1]

        queue = collections.deque()
        fresh = []
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh.append((r, c))

        time = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for i in range(4):
                    nr, nc = r+dr[i], c+dc[i]
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
            time += 1

        for r, c in fresh:
            if grid[r][c] == 1:
                return -1
                
        return time-1 if time else 0
