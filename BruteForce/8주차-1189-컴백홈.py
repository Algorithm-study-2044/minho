import sys

R, C, K = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(sys.stdin.readline().rstrip()))

ans = 0
dr, dc = [1, -1, 0, 0], [0, 0, -1, 1]

def dfs(r, c, dst):
    if r == 0 and c == C-1:
        if dst == K:
            global ans
            ans += 1
        return
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == '.':
            board[nr][nc] = 'T'
            dfs(nr, nc, dst+1)
            board[nr][nc] = '.'
    return

board[R-1][0] = 'T'  # initialization
dfs(R-1, 0, 1)
print(ans)
