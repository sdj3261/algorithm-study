import sys
from collections import deque

n,l,r = map(int,sys.stdin.readline().split())
q = deque()
arr = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dy = [-1,0,1,0]
dx = [0,1,0,-1]
tmp = deque()

def bfs(y,x) :
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
    

for i in range(n) :
    data = list(map(int,input().split()))
    for j in range(n) :
        arr[i][j] = data[j]
ret = 0

while True :
    flag = False
    visited = [[0] * n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            if visited[i][j] == 0 :
                country = bfs(i,j)
            #국경선 열리고 인구이동 시작
            if len(country) > 1 :
                flag = True
                number = sum([arr[y][x] for x,y in country]) // len(country)
                for x,y in country :
                    arr[y][x] = number
    #연합 해체 , 모든국경선 닫기
    if flag is False :
        break
    ret += 1
    

print(ret)
        

                
        
    
