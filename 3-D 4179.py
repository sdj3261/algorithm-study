from collections import deque
r,c = map(int,input().split())
arr = [["#"] * c for _ in range(r)]
visited = [[False] * c for _ in range(r)]
fire_check = [[994321] * c for _ in range(r)]
person_check = [[0] * c for _ in range(r)]
sy =0
sx = 0
q = deque()
dy = [-1,0,1,0]
dx = [0,1,0,-1]

#불의 최단거리보다 벽 막힘없이 더 빠르게 갈수있을때 성공 후 거리 계산 , 이외에는 impossible
ret = 0

def check(a,b) :
    return 0<=a and a<r and 0 <= b and b < c
    
    

for i in range(r) :
    data = list(input())
    for j in range(c) :
        #불의 pos 담기
        if data[j] == "F" :
            fire_check[i][j] = 1
            q.append((i,j))
        #시작위치 pos 담기
        elif data[j] == "J" :
            sy = i
            sx = j
        arr[i][j] = data[j]
        
#fire 거리 계산
while q :
    y,x = q.popleft()
    for i in range(4) :
        ny = dy[i] + y
        nx = dx[i] + x
        if not check(ny,nx) :
            continue
        if fire_check[ny][nx] != 994321 or arr[ny][nx] == "#" :
            continue
        fire_check[ny][nx] = fire_check[y][x] + 1
        q.append((ny,nx))

# 사람 시작위치 큐에 넣기
person_check[sy][sx] = 1
q.append((sy,sx))

#큐가 벽 가장자리 도착하거나 큐에 데이터가 없으면 종료
while q :
    y,x = q.popleft()
    if y == r-1 or x == c-1 or x == 0 or y == 0 :
        ret = person_check[y][x]
        break
    for i in range(4) :
        ny = dy[i] + y
        nx = dx[i] + x
        if not check(ny,nx) :
            continue
        if person_check[ny][nx] or arr[ny][nx] == "#" :
            continue
        if fire_check[ny][nx] <= person_check[y][x] + 1 :
            continue
        person_check[ny][nx] = person_check[y][x] + 1
        q.append((ny,nx))
if ret != 0 :
    print(ret)
else :
    print("IMPOSSIBLE")

