from collections import deque
n, m = map(int, input().split())
#
arr = [[] for _ in range(n+1)]
#
for i in range(m) :
    a, b = map(int, input().split())
    arr[b].append(a)

def bfs(x) :
    visited[x] = True
    q = deque()
    q.append(x)
    count = 1

    while q :
        x = q.popleft()
        for y in arr[x]:
            if not visited[y] :
                visited[y] = True
                count += 1
                q.append(y)
    return count

result_num = []
ret = 0
for i in range(1,n+1) :
     visited = [False] * (n + 1)
     cnt = bfs(i)

     ret = max(ret,cnt)
     if ret == cnt :
         result_num.append(i)
     elif ret < cnt :
         result_num.clear()
         result_num.append(cnt)



for i in sorted(result_num) :
     print(i,end= ' ')



# n, m = map(int, input().split())
#
# arr = [[] * (n+1) for _ in range(n+1)]
#
# for i in range(m) :
#     a,b = map(int, input().split())
#     arr[a].append(b)
#
# visited = [False] * (n+1)
# def dfs(x) :
#     visited[x] = True
#     if len(arr[x]) == 0 :
#         cnt = 0
#         for i in visited :
#             if i is True :
#                 cnt += 1
#         return x, cnt
#     for i in arr[x] :
#         if not visited[i] :
#             dfs(i)
#     return -1,-1
#
# ret = 0
# result_num = []
#
# for i in range(1,n+1) :
#     visited = [False] * (n + 1)
#     x, cnt = dfs(i)
#
#     if ret == cnt : #cnt랑 같으면 append
#         result_num.append(x)
#     if ret < cnt : # cnt가 더크면 append
#         ret = cnt
#         result_num.clear()
#         result_num.append(x)
#
# for i in sorted(result_num) :
#     print(i,end= ' ')
#
#
#
#
