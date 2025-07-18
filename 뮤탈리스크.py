from collections import deque
from itertools import permutations
n = int(input())
hp = list(map(int, input().split()))
visited = [[[False] * 61 for _ in range(61)] for _ in range(61)]

attacks = list(permutations([9,3,1]))

while len(hp) < 3 :
    hp.append(0)
ret = 0

def bfs() :

    q = deque() #모든 hp가 0이되는 지점 bfs 로 찾기
    q.append((hp[0], hp[1], hp[2], 0))
    visited[hp[0]][hp[1]][hp[2]] = True

    while q :
        data = q.popleft()

        x,y,z,ac = data
        if x == 0 and y == 0 and z == 0 :
            return ac

        for attack in attacks :
            d1,d2,d3 = attack
            x1 = max(x - d1, 0)
            y1 = max(y - d2, 0)
            z1 = max(z - d3, 0)
            if not visited[x1][y1][z1] :
                visited[x1][y1][z1] = True
                q.append((x1,y1,z1,ac+1))
    return 0

ac = bfs()
print(ac)






