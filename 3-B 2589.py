from collections import deque

n, m = map(int, input().split())
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

board = [[' '] * m for _ in range(n)]
q = deque()
posL = deque()

def bfs(y, x):
    visited = [[0] * m for _ in range(n)]
    visited[y][x] = 1
    q.append((y, x))
    ret = 0

    while q:
        qy, qx = q.popleft()
        for i in range(4):
            ny = dy[i] + qy
            nx = dx[i] + qx

            if ny < 0 or ny >= n or nx < 0 or nx >= m or visited[ny][nx] or board[ny][nx] == "W":
                continue
            if board[ny][nx] == "L" and visited[ny][nx] == 0:
                visited[ny][nx] = visited[qy][qx] + 1
                q.append((ny, nx))
                ret = max(ret,visited[ny][nx])
    return ret-1


for i in range(n):
    data = input()
    for j in range(m):
        board[i][j] = data[j]
        if board[i][j] == "L":
            posL.append((i, j))

ret2 = float('-inf')
for posY,posX in posL :
    visited = [[0] * m for _ in range(n)]
    ret2 = max(ret2, bfs(posY,posX))
    
print(ret2)
