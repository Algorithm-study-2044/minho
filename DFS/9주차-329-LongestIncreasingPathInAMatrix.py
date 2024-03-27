from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        visited = [[0] * n for _ in range(m)]
        dr, dc = [1, -1, 0, 0], [0, 0, -1, 1]

        def dfs(r, c):
            if visited[r][c]:
                return visited[r][c]

            visited[r][c] = 1
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    visited[r][c] = max(visited[r][c], dfs(nr, nc)+1)
                    
            return visited[r][c]

        rslt = 1
        for r in range(m):
            for c in range(n):
                rslt = max(rslt, dfs(r, c))
        return rslt
