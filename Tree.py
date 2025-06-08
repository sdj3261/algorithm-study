n = int(input())
parents =list(map(int, input().split()))
tree = [[] for _ in range(n)]
ret = 0
delete_node = int(input())
root = -1
for child in range(n) :
    parent = parents[child]
    if parent == -1:
        root = child  # 루트 노드 저장
    else:
        tree[parent].append(child)


def dfs(node) :
    global ret, root
    if node == delete_node :
        return
    if not tree[node] :
        ret += 1
        return

    # 삭제되지않은 노드가 하나도 없으면 리프노드
    is_leaf = True
    for child in tree[node] :
        if child != delete_node :
            dfs(child)
            is_leaf = False
    if is_leaf :
        ret += 1
        return

if delete_node == root:
    print(0)
else:
    dfs(root)
    print(ret)



