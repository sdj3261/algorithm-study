from copy import deepcopy
from itertools import combinations
# 벽 무조건 3개를 세우고 다시 뺴고.. 하면서 가장 안전영역의 크기가 클때의 최대값 구하기.. 완탐으로갑시다
# 8c3 .. + 이중루프
n,m = map(int,input().split())
arr = [[0] * (m+4) for _ in range(n+4)]
visited = [[False] * (m+4) for _ in range(n+4)]

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def dfs(map, y, x) :
    visited[y][x] = 1
    for i in range(4) :
        ny = dy[i] + y
        nx = dx[i] + x

        if ny < 0 or ny >= n or nx < 0 or nx >= m or visited[ny][nx] or map[ny][nx] != 0 :
            continue
        if map[ny][nx] == 0 :
            map[ny][nx] = 2
        dfs(map,ny,nx)
def checkSafeZone(board) :
    cnt = 0
    for i in range(n) :
        for j in range(m) :
            if board[i][j] == 0 :
                cnt += 1
    return cnt
        
safe_position = []
virus_position = []
for i in range(n) :
    data = input().split()
    for j in range(m) :
        arr[i][j] = int(data[j])
        if(arr[i][j] == 0) :
            safe_position.append((i,j))
        elif(arr[i][j] == 2) :
            virus_position.append((i,j))
ret = 0 
safe_combis = list(combinations(safe_position,3))
for safe_combi in safe_combis :
    board = deepcopy(arr)
    board[safe_combi[0][0]][safe_combi[0][1]] = 1
    board[safe_combi[1][0]][safe_combi[1][1]] = 1
    board[safe_combi[2][0]][safe_combi[2][1]] = 1
    visited = [[False] * (m+4) for _ in range(n+4)]

    for pos in virus_position :
        dfs(board,pos[0],pos[1])
    ret = max(ret, checkSafeZone(board))

print(ret)

            
            


