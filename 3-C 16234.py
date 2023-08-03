from collections import deque

n, l, r = map(int, input().split())
arr = [[0] * n for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        arr[i][j] = data[j]

def bfs(y, x, visited):  # Pass visited as an argument
    q = deque()
    tmp = deque()
    visited[y][x] = 1
    q.append((y, x))
    tmp.append((y, x))
    while q:
        qy, qx = q.popleft()

        for i in range(4):
            ny = qy + dy[i]
            nx = qx + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n or visited[ny][nx] == 1:
                continue
            if l <= abs(arr[ny][nx] - arr[qy][qx]) <= r:  # Use (qy, qx) instead of (y, x)
                q.append((ny, nx))
                tmp.append((ny, nx))
                visited[ny][nx] = 1

    return tmp

ret = 0

while True:
    flag = False
    visited = [[0] * n for _ in range(n)]  # Initialize visited here
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                count = bfs(i, j, visited)  # Pass visited as an argument
                if len(count) > 1:
                    flag = True
                    number = sum([arr[y][x] for y, x in count]) // len(count)
                    for y, x in count:
                        arr[y][x] = number
    if not flag:
        break
    ret += 1

print(ret)
