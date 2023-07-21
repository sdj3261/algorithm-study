from collections import deque
n,m = map(int,input().split())
board = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for i in range(m) :
    a,b = map(int,input().split())
    board[b].append(a)

def bfs(i) :
    visited = [0] * (n + 1)
    visited[i] = True
    q = deque([i])
    cnt = 1
    while q :
        data = q.popleft()
        for v in board[data] :
            if not visited[v] :
                q.append(v)
                visited[v] = True
                cnt+=1
    return cnt
max_cnt = 0
ret = []
for i in range(1,n+1) :
    cnt = bfs(i)
    if cnt > max_cnt :
        max_cnt = cnt
        ret = []
        ret.append(i)
    elif cnt == max_cnt :
        ret.append(i)
    else :
        pass
        
print(*ret)
    