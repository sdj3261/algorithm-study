t = int(input())
for i in range(t):
    clothes = set()
    m = dict()
    n = int(input())
    for j in range(n):
        name, kind = input().split()
        clothes.add(kind)
        if kind not in m:
            m[kind] = 1
        elif kind in m:
            m[kind] += 1
    #key가 1개인지 여러개인지 확인
    ret = 1
    for k, v in m.items():
        ret *= (v + 1)
    print(ret - 1)
