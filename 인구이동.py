import sys
sys.setrecursionlimit(10000)
n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#인구  이동 하루동안 진행
# 국경선을 공유하는 두 나라의 인구차이가 l명 이상, r명 이하라면 국경선 open
# 이동 시작
# 이동가능하면 그 나라들은 연합
# 각 칸 인구수는 연합의 인구수 다 더한거 / 연합을 이루는 칸의 개수 소수점은 버림
# 연합 헤체
# 인구이동이 없을때까지 지속된다. 인구이동은 최대 2000번
# 며칠동안 발생했는지

def peopleMoveCheck(y, x, visited, union):
    visited[y][x] = True
    union.append((y, x))
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
            if l <= abs(arr[y][x] - arr[ny][nx]) <= r:
                peopleMoveCheck(ny, nx, visited, union)

ret = 0
while True:
    visited = [[False]*n for _ in range(n)]
    moved = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union = []
                peopleMoveCheck(i, j, visited, union)
                if len(union) > 1:
                    moved = True
                    total = sum(arr[y][x] for y, x in union)
                    avg = total // len(union)
                    for y, x in union:
                        arr[y][x] = avg

    if not moved:
        break
    ret += 1

print(ret)




