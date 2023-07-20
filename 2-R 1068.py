n = int(input())
parent_node = list(map(int, input().split()))
del_node = int(input())

tree = {}
for i in range(n):
    if parent_node[i] == del_node or i == del_node :
        continue
    if parent_node[i] in tree:
        tree[parent_node[i]].append(i)
    else:
        tree[parent_node[i]] = [i]
print(tree)
# 리프 노드 개수 세기
leaf_count = 0
if -1 in tree :
    que = [-1]
else :
    que = []
while que :
    node = que.pop()
    if node not in tree :
        leaf_count += 1 
    else :
        que.extend(tree[node])
    

print(leaf_count)
