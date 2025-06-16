from collections import deque
dy = [-1,0,1,0]
dx = [0,1,0,-1]

n, m = map(int, input().split())
arr = [['0'] * m for _ in range(n)]

visited = [[-1] * m for _ in range(n)]
land_data = []

for i in range(n) :
    data = input()
    for j in range(m) :
        arr[i][j] = data[j]
        if arr[i][j] == 'L' :
            land_data.append((i, j)) #땅 위치 저장
q = deque()
ret = 0

def bfs(y,x) :
    q.append((y,x))
    visited[y][x] = 0
    bfs_ret = 0
    while q :
        qy,qx = q.popleft()
        for i in range(4) :
            ny = dy[i] + qy
            nx = dx[i] + qx

            if ny < 0 or ny >= n or nx < 0 or nx >= m or visited[ny][nx] >= 0 :
                continue
            if arr[ny][nx] == 'W' : #물이면
                continue
            if arr[ny][nx] == 'L' :
                q.append((ny,nx))
                visited[ny][nx] = visited[qy][qx] + 1 #이동시 업데이트
                bfs_ret = max(bfs_ret, visited[ny][nx])
    return bfs_ret



for y,x in land_data :
    visited = [[-1] * m for _ in range(n)]
    #bfs 다른 L과의 최대 거리 저장
    ret = max(ret,bfs(y,x))

print(ret)



