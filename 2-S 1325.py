n,m = map(int,input().split())
tree = {}
ret = []
cnt = {}
index = {}
# 초기화
for i in range(n) :
    index[i+1] = 0
# 단방향 간선 만들기
for i in range(m) :
    a,b = map(int,input().split())
    if a in tree.keys() :
        tree[a].append(b)
    else :
        tree[a] = [b]

#각 번호에 대한 해킹 가능 수 카운팅
for i in range(1,n+1) :
    que = []
    que.append(i)
    while que :
        data = que.pop()
        for key, values in tree.items() :
            if data in values :
                que.append(key)
                index[i] += 1
                
max_value = max(index.values())
ret = [key for key, value in index.items() if value == max_value]
print(" ".join(map(str, ret)))