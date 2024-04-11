import sys

## Solution1 - set
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

answer = float("INF")
cant = set()

dr, dc = [0, 1, -1, 0, 0], [0, 0, 0, -1, 1]

def dfs(cost, depth):
    global answer
    if answer <= cost:
        return
    if depth == 3:
        answer = cost
        return
    
    for r in range(1, N-1):
        for c in range(1, N-1):
            check = 0
            for i in range(5):
                nr, nc = r+dr[i], c+dc[i]
                if (nr, nc) in cant:
                    check = 1
                    break
            if check:
                continue
            for i in range(5):
                nr, nc = r+dr[i], c+dc[i]
                check += board[nr][nc]
                cant.add((nr, nc))

            dfs(cost+check, depth+1)

            for i in range(5):
                nr, nc = r+dr[i], c+dc[i]
                cant.remove((nr, nc))

dfs(0, 0)
print(answer)


## Solution2 - list
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

answer = float("INF")
visited = [[0] * N for _ in range(N)]

dr, dc = [0, 1, -1, 0, 0], [0, 0, 0, -1, 1]

def dfs(cost, depth):
    global answer
    if answer <= cost:
        return
    if depth == 3:
        answer = cost
        return
    
    for r in range(1, N-1):
        for c in range(1, N-1):
            check = 0
            for i in range(5):
                nr, nc = r+dr[i], c+dc[i]
                if visited[nr][nc]:
                    check = 1
                    break
            if check:
                continue
            for i in range(5):
                nr, nc = r+dr[i], c+dc[i]
                check += board[nr][nc]
                visited[nr][nc] = 1

            dfs(cost+check, depth+1)

            for i in range(5):
                nr, nc = r+dr[i], c+dc[i]
                visited[nr][nc] = 0

dfs(0, 0)
print(answer)
