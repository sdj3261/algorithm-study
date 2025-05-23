import sys
sys.setrecursionlimit(10**6)
t = int(input())
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def dfs(y, x, board, visited, n, m):
    visited[y][x] = True
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if 0 <= ny < n and 0 <= nx < m:
            if not visited[ny][nx] and board[ny][nx] == 1:
                dfs(ny, nx, board, visited, n, m)


for _ in range(t):
    n, m, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())
        board[y][x] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and not visited[i][j]:
                dfs(i, j, board, visited, n, m)
                cnt += 1

    print(cnt)
