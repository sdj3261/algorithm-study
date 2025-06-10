from collections import deque
n, m = map(int, input().split())
board = [[0] * m for _ in range(n)]
dy = [0,1,0,-1]
dx = [1,0,-1,0]
visited = [[False] * m for _ in range(n)]


:quit()