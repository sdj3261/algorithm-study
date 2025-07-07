from collections import deque
r,c = map(int,input().split())
arr = [['0'] * c for i in range(r)]
j_arr = [[-1] * c for i in range(r)]
f_arr = [[-1] * c for i in range(r)]
for i in range(r):
    arr[i] = input()
j_y = 0
j_x = 0
dy = [-1,0,1,0]
dx = [0,1,0,-1]
fire_set = set()
for i in range(r) :
    for j in range(c) :
        if arr[i][j] == 'J' :
            j_y = i
            j_x = j
            j_arr[i][j] = 0
        if arr[i][j] == 'F' :
            fire_set.add((i,j))
            f_arr[i][j] = 0

#지훈이의 최단거리 배열 생성
q = deque()
q.append((j_y,j_x))
while q :
    y,x = q.popleft()
    for i in range(4) :
        ny = dy[i] + y
        nx = dx[i] + x
        if ny < 0 or ny >= r or nx < 0 or nx >= c :
            continue
        if arr[ny][nx] == '.' and j_arr[ny][nx] == -1:
            q.append((ny,nx))
            j_arr[ny][nx] = j_arr[y][x] + 1

#fire 배열 최단거리 측정
q = deque()
for y,x in fire_set :
    q.append((y,x))
while q :
    y,x = q.popleft()
    for i in range(4) :
        ny = dy[i] + y
        nx = dx[i] + x
        if ny < 0 or ny >= r or nx < 0 or nx >= c :
            continue
        if arr[ny][nx] == '.' and f_arr[ny][nx] == -1 :
            q.append((ny,nx))
            f_arr[ny][nx] = f_arr[y][x] + 1

j_min_data = float('inf')
for i in range(r):
    for j in range(c):
        if i == r-1 or j == c-1 or i == 0 or j == 0:
            if arr[i][j] == '#':
                continue
            if j_arr[i][j] == -1:
                continue
            # 불이 안 오는 칸이면 무조건 탈출 가능
            if f_arr[i][j] == -1:
                j_min_data = min(j_min_data, j_arr[i][j])
            elif f_arr[i][j] > j_arr[i][j]:
                j_min_data = min(j_min_data, j_arr[i][j])

if j_min_data == float('inf') :
    print("IMPOSSIBLE")
else :
    print(j_min_data + 1)






