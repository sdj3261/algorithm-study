from itertools import combinations
from copy import deepcopy

n,m = map(int,input().split())
arr = [[0] * (m+4) for _ in range(n+4)]
dy = [-1,0,1,0]
dx = [0,1,0,-1]
safe = []
virus = []

def dfs(grid, y, x):
    visited[y][x] = True
    grid[y][x] = 2
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x

        if ny < 0 or ny >= n or nx < 0 or nx >= m or visited[ny][nx] or grid[ny][nx] != 0:
            continue

    
        dfs(grid, ny, nx)
        
def safe_count(grid):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                cnt += 1
    return cnt

# 입력받기
for i in range(n) :
    line = input().split()
    for j in range(m) :
        arr[i][j] = int(line[j])
        if arr[i][j] == 0 :
            safe.append((i,j))
        elif arr[i][j] == 2 :
            virus.append((i,j))

zero_combi = list(combinations(safe, 3))
max_safe_count = 0
idx = 0
for combi in zero_combi:
    board = deepcopy(arr)
    for wall in combi:
        board[wall[0]][wall[1]] = 1
    visited = [[False] * m for _ in range(n)]
    for v in virus:
        dfs(board, v[0], v[1])

    safe_cnt = safe_count(board)
    max_safe_count = max(max_safe_count, safe_cnt)

print(max_safe_count)
            
    
                
            
            



            
                