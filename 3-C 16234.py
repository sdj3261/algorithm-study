import sys
from collections import deque

n,l,r = map(int,sys.stdin.readline().split())
arr = [[0] * n for _ in range(n)]
dy = [-1,0,1,0]
dx = [0,1,0,-1]


for i in range(n) :
    data = list(map(int,input().split()))
    for j in range(n) :
        arr[i][j] = data[j]

def bfs(y,x) :
    q = deque()
    tmp = deque()
    visited[y][x] = 1
    q.append((y,x))
    tmp.append((y,x))
    while q :
        qy,qx = q.popleft()

        for i in range(4) :
            ny = qy + dy[i]
            nx = qx + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n or visited[ny][nx] == 1 :
                continue
            if l <= abs(arr[ny][nx] - arr[y][x]) <= r : 
                q.append((ny,nx))
                tmp.append((ny,nx))
                visited[ny][nx] = 1
    return tmp
    
ret = 0

while True :
    flag = False
    for i in range(n) :
        for j in range(n) :
            visited = [[0] * n for _ in range(n)]
            count = bfs(i,j)
        
            #bfs에 들어간 좌표가 2개 이상 있다면 연합 이동 시작
            if len(count) >= 2 :
                flag = True
                number = sum([arr[y][x] for y, x in count]) // len(count)
                for y,x in count :
                    arr[y][x] = number
                    print(arr[y][x])
    if flag == False :
        break
    ret += 1

print(ret)
    
                
                
                    
                
            
            
            
        
        

                
        
    
