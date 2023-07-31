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
    tmp = input().split()
    for j in range(n) :
        if int(tmp[j]) == 2 :
            chicken.append((i,j))
        elif int(tmp[j]) == 1 :
            home.append((i,j))
            
        board[i][j] = int(tmp[j])


# 도시의 치킨거리가 가장 최솟값 구하기 완탐 2번 개수 Combination m 하여 모든 경우의 수 구하기

chicken_combis = list(combinations(chicken,m))
ret = 1000000
# 치킨 combi 개수
for chicken_combi in chicken_combis :
    sum = 0
    # home 뽑아내기
    for h in home :
        ccd = 1000000
        # 치킨집 m개에 대해 최솟값
        for k in range(m) :
            ccd = min(ccd, dist(h[0],h[1],chicken_combi[k][0],chicken_combi[k][1]))
        sum += ccd
    ret = min(ret, sum)

print(ret)





        


