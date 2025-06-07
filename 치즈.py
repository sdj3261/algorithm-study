from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True

    melt_list = []

    while queue:
        print(queue)
        y, x = queue.popleft()
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                visited[ny][nx] = True
                if board[ny][nx] == 0:
                    queue.append((ny, nx))
                elif board[ny][nx] == 1:
                    # 외부 공기와 접촉한 치즈 → 녹일 대상으로 추가
                    melt_list.append((ny, nx))

    return melt_list

time = 0
last_cheese = 0

while True:
    melt_target = bfs()
    # 디버깅용 출력: 녹을 위치는 1, 나머지는 0
    print("MELT!!!!!!")
    for i in range(n):
        for j in range(m):
            if (i, j) in melt_target:
                print(1, end=' ')
            else:
                print(0, end=' ')
        print()  # 줄 바꿈
    if not melt_target:
        break

    last_cheese = len(melt_target)
    for y, x in melt_target:
        board[y][x] = 0  # 치즈 녹이기

    time += 1

print(time)
print(last_cheese)
