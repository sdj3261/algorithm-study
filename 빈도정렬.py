n,c = map(int,input().split())
data = list(map(int,input().split()))


dic = dict()

for i in data:
    if i not in dic:
        dic[i] = 0

    dic[i] += 1


dic = sorted(dic.items(), key=lambda x: -x[1])
print(dic.items())

for a, b in dic:
    for j in range(b):
        print(str(a)+" ",end="")
