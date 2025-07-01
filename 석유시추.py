def solution(land):
    if not land or not land[0]:
        return 0

    n = len(land)
    m = len(land[0])
    visited = [[False] * m for _ in range(n)]
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    oil_per_col = [0] * m

    def dfs(y, x):
        stack = [(y, x)]
        visited[y][x] = True
        size = 0
        cols = set()

        while stack:
            cy, cx = stack.pop()
            size += 1
            cols.add(cx)

            for dir in range(4):
                ny = cy + dy[dir]
                nx = cx + dx[dir]

                if 0 <= ny < n and 0 <= nx < m:
                    if not visited[ny][nx] and land[ny][nx] == 1:
                        visited[ny][nx] = True
                        stack.append((ny, nx))

        return size, cols

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j] == 1:
                size, cols = dfs(i, j)
                for col in cols:
                    oil_per_col[col] += size

    return max(oil_per_col) if oil_per_col else 0
