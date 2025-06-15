from collections import deque
n,m = map(int,input().split())
arr = [[0] * m for _ in range(n)]
q = deque()
dy = [-1,0,1,0]
dx = [0,1,0,-1]

for i in range(n) :
    data = list(map(int,input().split()))
    for j in range(m) :
        arr[i][j] = data[j]

ret1 = 0
ret2 = 0
cnt = 0

def bfs(y,x) :
    visited = [[False] * m for _ in range(n)]
    visited[y][x] = True
    q.append((y,x))
    melt_cheese = []

    while q :
        y,x = q.popleft()
        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m :
                continue
            if visited[ny][nx] :
                continue
            if arr[ny][nx] == 0 :
                q.append((ny,nx))
                visited[ny][nx] = True
            if arr[ny][nx] == 1 :
                melt_cheese.append((ny,nx))
                visited[ny][nx] = True

    #겉면 녹이기
    for cheese in melt_cheese :
        y,x = cheese
        arr[y][x] = 0

    return len(melt_cheese)

while True :
    melt_count = bfs(0,0)

    if melt_count == 0 :
        break
    else :
        ret2 = melt_count
    cnt += 1
print(cnt)
print(ret2)








