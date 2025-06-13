n = int(input())
parent_node = list(map(int, input().split()))
del_node = int(input())

arr = [[] for _ in range(n)]
visited = [False for _ in range(n)]

# 트리 만들기 + 루트 찾기
for i in range(n):
    if parent_node[i] == -1:
        root = i
    else:
        arr[parent_node[i]].append(i)

# 🔥 삭제 노드를 부모의 자식 리스트에서 제거
if parent_node[del_node] != -1:
    arr[parent_node[del_node]].remove(del_node)

ret = 0
def dfs(x):
    global ret
    visited[x] = True
    if len(arr[x]) == 0:
        ret += 1
        return
    for j in arr[x]:
        if not visited[j]:
            dfs(j)

if del_node == root:
    print(0)
else:
    dfs(root)
    print(ret)
