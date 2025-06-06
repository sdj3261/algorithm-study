n, m = map(int,input().split())
board = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dy = [0,1,0,-1]
dx = [1,0,-1,0]
ret = 0

safe_zone = []
for i in range(n) :
    data = list(map(int, input().split()))
    for j in range(m) :
        board[i][j] = data[j]
        if data[j] == 0 :
            safe_zone.append((i,j))

def dfs(y,x) :
    visited[y][x] = True
    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= n or nx < 0 or nx >= m or visited[ny][nx] == True :
            continue
        if board[ny][nx] == 1 :
            continue
        if board[ny][nx] == 0 :
            dfs(ny, nx)




# 벽세우기 작업
for i in range(len(safe_zone) - 2) :
    for j in range(i+1,len(safe_zone)-1) :
        for k in range(j+1,len(safe_zone)) :
            safe_count = 0
            visited = [[False] * m for _ in range(n)]
            safe_wall1 = safe_zone[i]
            safe_wall2 = safe_zone[j]
            safe_wall3 = safe_zone[k]
            board[safe_wall1[0]][safe_wall1[1]] = 1
            board[safe_wall2[0]][safe_wall2[1]] = 1
            board[safe_wall3[0]][safe_wall3[1]] = 1

            for l in range(n) :
                for v in range(m) :
                    if board[l][v] == 2 :
                        dfs(l,v) #바이러스 퍼뜨리기

            for l in range(n) :
                for v in range(m) :
                    if visited[l][v] == False and board[l][v] == 0 :
                        safe_count += 1


            ret = max(ret, safe_count)

            board[safe_wall1[0]][safe_wall1[1]] = 0
            board[safe_wall2[0]][safe_wall2[1]] = 0
            board[safe_wall3[0]][safe_wall3[1]] = 0

print(ret)





