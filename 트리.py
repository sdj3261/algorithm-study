n = int(input())
parent_node = list(map(int, input().split()))
del_node = int(input())

tree = [[] for _ in range(n)]
root = -1

for i in range(n):
    if parent_node[i] == -1:
        root = i
    else:
        tree[parent_node[i]].append(i)

def dfs(node):
    if node == del_node:
        return 0
    if not tree[node] or (len(tree[node]) == 1 and tree[node][0] == del_node):
        return 1
    cnt = 0
    for child in tree[node]:
        if child != del_node:
            cnt += dfs(child)
    return cnt

print(0 if del_node == root else dfs(root))
