from collections import deque
n, m = map(int, input().split())
board = [[0] * m for _ in range(n)]
dy = [0,1,0,-1]
dx = [1,0,-1,0]
visited = [[False] * m for _ in range(n)]

cheese_count = 0

for i in range(n) :
    data = list(map(int,input().split()))
    for j in range(m) :
        board[i][j] = data[j]


def bfs() :
    visited = [[False] * m for _ in range(n)]
    melt = []
    q = deque()
    q.append((0,0))
    visited[0][0] = True
    while q :
        y,x = q.popleft()

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m :
                if visited[ny][nx]  :
                    continue
                if board[ny][nx] == 0 :
                    q.append((ny,nx))
                    visited[ny][nx] = True
                    #이 0자리로는 이제 탐색안합니다.
                if board[ny][nx] == 1 :
                    melt.append((ny,nx))
                    visited[ny][nx] = True
                    #이 치즈로는 이제 탐색 안합니다.
    return melt

time = 0
latest_cheese = 0 #

while True :
    melt_idx = bfs()
    if len(melt_idx) == 0:
        break
    #melt 존재시 녹이기 수행
    for melt in melt_idx :
        melt_y,melt_x = melt
        board[melt_y][melt_x] = 0
    latest_cheese = len(melt_idx)
    time += 1

print(time)
print(latest_cheese)
