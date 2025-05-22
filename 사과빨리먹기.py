board = [[0] * 5 for _ in range(5)]
for i in range(5) :
    board[i] = list(map(int,input().split()))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
y, x = map(int,input().split())
visited = [[False] * x for _ in range(y)]

def dfs(r,c) :
    data = 0
    visited[r][c] = True
    for i in range(4) :
        ny = dy[i] + y
        nx = dx[i] + x
        if 0 > ny or ny >= y or 0 > nx or nx >= x or visited[ny][nx] == False :
            continue
        if board[ny][nx] == -1 :
            continue
        if board[ny][nx] == 1 :
            data += dfs(ny,nx)
        if board[ny][nx] == 1 :
            dfs(ny,nx)
        data += dfs(ny,nx)
    return data
    
