import sys
sys.setrecursionlimit(10 ** 6)
a = int(input())
height = 0
max_height = 0
dy = [-1,0,1,0]
dx = [0,1,0,-1]
ret = 0
max_ret = 0
visited = [[False] * a for _ in range(a)]

def dfs(y,x,height) :
    visited[y][x] = True
    for i in range(4) :
        ny = dy[i] + y
        nx = dx[i] + x
        if ny < 0 or ny >= a or nx < 0 or nx >= a or visited[ny][nx] or board[ny][nx] == -1 :
            continue
        dfs(ny,nx,height)
    
def coloringBoard(arr, height) :
    for i in range(a) :
        for j in range(a) :
            if arr[i][j] <= height :
                arr[i][j] = -1

board = [[0] * a for _ in range(a)]
for i in range(a) :
    data = list(map(int,input().split()))
    for j in range(a) :
        board[i][j] = data[j]
        max_height = max(max_height, data[j])
        height = min(height, data[j])
        

original = [row[:] for row in board]

for k in range(height,max_height+1) :
    board = [row[:] for row in original]
    visited = [[False] * a for _ in range(a)]
    coloringBoard(board, k)
    ret = 0
    for i in range(a) :
        for j in range(a) :
            if board[i][j] != -1 and not visited[i][j] :
                dfs(i,j,k)
                ret += 1
    max_ret = max(max_ret, ret)
print(max_ret)
                
                
            
        
            
            
        
        
            


    
    
