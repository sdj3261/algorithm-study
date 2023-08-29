def dist(x1,y1,x2,y2) :
    return abs(x1-x2) + abs(y1-y2)

from collections import deque
from itertools import combinations

n, m = map(int, input().split())
board = [[0] * (n+1) for _ in range(n+1)]
visited =[[False] for _ in range (n+1)]
chicken = deque()
home = deque()

for i in range(n) :
    data = input().split()
    for j in range(n) :
        board[i][j] = int(data[j])
        if board[i][j] == 1 :
            home.append((i,j))
        elif board[i][j] == 2 :
            chicken.append((i,j))

# 최대 m개를 골랐을때 도시의 치킨거리 최솟값 구하기
# import sys
# maximum = sys.maxint
# minimum = sys.minint

combi = list(combinations(chicken,m)) # (1,2) (2,2), (4,4) 좌표값
ret = float("inf")

for c in combi :
    sum = 0
    for h in home :
        minDist = float("inf")
        for k in range(m) :
            minDist = min(minDist,dist(c[k][0],c[k][1],h[0],h[1]))
        sum += minDist
    ret = min(ret,sum)
print(ret)
            
            
        
        






        


