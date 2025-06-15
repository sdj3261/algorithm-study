from collections import deque

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(sy, sx):
    visited = [[-1] * m for _ in range(n)]
    q = deque()
    q.append((sy, sx))
    visited[sy][sx] = 0
    max_dist = 0

    while q:
        y, x = q.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < n and 0 <= nx < m:
                if arr[ny][nx] == 'L' and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x] + 1
                    max_dist = max(max_dist, visited[ny][nx])
                    q.append((ny, nx))
    return max_dist

# 모든 'L'에서 BFS 돌려서 최댓값 찾기
answer = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            answer = max(answer, bfs(i, j))

print(answer)
