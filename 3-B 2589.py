from collections import deque
from itertools import combinations
import sys


q = deque()
dy = [-1,0,1,0]
dx = [0,1,0,-1]
land = []

def bfs(y,x) :
    visited = [[0] * m for _ in range(n)]
    visited[y][x] = 1
    ret = 0
    q.append((y,x))
    while q :
        y,x= q.popleft()
        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]
            
            if(ny < 0 or ny >= n or nx < 0 or nx >= m or visited[ny][nx]) :
                continue
            elif board[ny][nx] == 'L' and visited[ny][nx] == False :
                visited[ny][nx] = visited[y][x] + 1
                ret = max(ret,visited[ny][nx])
                q.append((ny,nx))
    return ret-1

n,m = map(int,input().split())
board = [[' '] * (m) for _ in range(n)]
for i in range(n) :
    data = list(input())
    for j in range(m) :
        board[i][j] = data[j]
        if board[i][j] == 'L' :
            land.append((i,j))

ret = -1000000
          
for l in land :
    ret = max(ret,bfs(l[0],l[1]))
print(ret)
    
    
    

        


        
        
        