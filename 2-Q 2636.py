import sys

visited = [[False] * 104 for _ in range(104)]
arr = [[0] * 104 for _ in range(104)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
edge = []
m, n = map(int, input().split())
sys.setrecursionlimit(10**6)

finalCheeseCount = 0  # finalCheeseCount를 전역 변수로 선언


def dfs(board, y, x):
    global finalCheeseCount  # finalCheeseCount를 전역 변수로 사용
    visited[y][x] = True
    if board[y][x] == 1:
        edge.append((y, x))
        finalCheeseCount += 1
        return

    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x

        if ny < 0 or ny >= m or nx < 0 or nx >= n or visited[ny][nx]:
            continue
        dfs(board, ny, nx)


def checkCheese():
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                return True
    return False


for i in range(m):
    data = input().split()
    for j in range(n):
        arr[i][j] = int(data[j])

dfs(arr, 0, 0)
ret1 = 0
ret2 = 0
while checkCheese():
    if len(edge) > 0:
        finalCheeseCount = len(edge)
    while edge:
        egY, egX = edge.pop()
        arr[egY][egX] = 0
    ret1 += 1
    visited = [[False] * 104 for _ in range(104)]
    dfs(arr, 0, 0)

print(ret1, end="\n")
print(finalCheeseCount, end="\n")
