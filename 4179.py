from collections import deque

INF = float('inf')   # 진짜 무한대 표현
n, m = map(int, input().split())

a = []
for _ in range(n):
    a.append(list(input().strip()))

fire_check = [[INF] * m for _ in range(n)]
person_check = [[0] * m for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

q = deque()

# fire 시작 좌표들 먼저 넣고 초기화
for i in range(n):
    for j in range(m):
        if a[i][j] == 'F':
            fire_check[i][j] = 1
            q.append((i, j))
        elif a[i][j] == 'J':
            sy, sx = i, j

# BFS: 불 먼저 확산
while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if fire_check[ny][nx] == INF and a[ny][nx] != '#':
                fire_check[ny][nx] = fire_check[y][x] + 1
                q.append((ny, nx))

# BFS: 사람 이동
q = deque()
person_check[sy][sx] = 1
q.append((sy, sx))
ret = 0

while q:
    y, x = q.popleft()
    # 테두리 탈출
    if y == 0 or y == n - 1 or x == 0 or x == m - 1:
        ret = person_check[y][x]
        break
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if person_check[ny][nx] == 0 and a[ny][nx] != '#':
                # 불보다 먼저 도착할 수 있어야 한다
                if fire_check[ny][nx] > person_check[y][x] + 1:
                    person_check[ny][nx] = person_check[y][x] + 1
                    q.append((ny, nx))

if ret != 0:
    print(ret)
else:
    print("IMPOSSIBLE")
