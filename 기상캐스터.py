from collections import deque
h,w = map(int,input().split())

ret = [[-1] * w for _ in range(h)]
board = []
q = deque()


for i in range(h):
    data = input()
    board.append(data)
    for j in range(w):
        if board[i][j] == 'c' :
            q.append((i,j))
            ret[i][j] = 0

while q :
    i,j = q.popleft()
    #i,j를 꺼낸후 1,2, 카운팅 시작한다.
    ret[i][j] = 0

    for k in range(j,w-1) :
        ret[i][k+1] = ret[i][k] + 1

for i in range(len(ret)) :
    for j in range(len(ret[i])) :
        print(ret[i][j], end = " ")
    print()




