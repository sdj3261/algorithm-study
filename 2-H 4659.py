n,c = map(int,input().split())
arr = list(map(int,input().split()))

m = dict()
for i in arr :
    if i in m :
        m[i] += 1
    else :
        m[i] = 1

sorted_arr = sorted(m.keys(),key=lambda x:-m[x])
ret = []
for i in sorted_arr :
    print(m[i] * (str(i) + " "), end = "")