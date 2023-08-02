import sys
from collections import deque
sys.setrecursionlimit(10**6)
m,n,k = map(int, sys.stdin.readline().split())  
arr = [[0] * n for _ in range(m)]
visited = [[0] * n for _ in range(m)]
q = deque()

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def dfs(y,x) :
    visited[y][x] = 1
    ret = 1
    
    for i in range(4) :
        ny = dy[i] + y
        nx = dx[i] + x

        if ny < 0 or ny >= m or nx < 0 or nx >= n or visited[ny][nx] == 1 or arr[ny][nx] == 1:
            continue
        if visited[ny][nx] == 0 :
            ret += dfs(ny,nx)
    return ret

for i in range(k) :
    data = list(map(int,sys.stdin.readline().split()))
    q.append((data[0],data[1]))
    q.append((data[2],data[3]))

while q :
    x1,y1 = q.popleft()
    x2,y2 = q.popleft()
    for i in range(y1,y2) :
        for j in range(x1,x2) :
            arr[i][j] = 1
squares = []
cnt = 0
for i in range(m) :
    for j in range(n) :
        if arr[i][j] == 0 and visited[i][j] == 0:
            cnt+=1
            square = dfs(i,j)
            squares.append(square)
print(cnt)
sorted_squares = sorted(squares)
print(*sorted_squares)
        
    
        
        