import sys
sys.setrecursionlimit(10**6)
m,n,k = map(int,input().split())
board = [[0] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]
dy = [-1,0,1,0]
dx = [0,1,0,-1]
square_arr = []
ret = 0

for i in range(k) :
    x1,y1,x2,y2 = map(int,input().split())
    for j in range(y1,y2) :
        for k in range(x1,x2) :
            board[j][k] = -1

def dfs(y,x) :
    visited[y][x] = True
    dfs_ret = 1
    for i in range(4) :
        ny = dy[i] + y
        nx = dx[i] + x
        if ny < 0 or ny >= m or nx < 0 or nx >= n or visited[ny][nx] or board[ny][nx] == -1 :
            continue
        if board[ny][nx] == 0 :
            dfs_ret += dfs(ny,nx)
    return dfs_ret

for i in range(m) :
    for j in range(n) :
        if board[i][j] == 0 and not visited[i][j]:
            ret+=1
            square_arr.append(dfs(i,j))
print(ret)
for i in sorted(square_arr, key=lambda x: x):
    print(i, end=" ")

    

