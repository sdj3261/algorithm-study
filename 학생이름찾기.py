d = dict()
a = list(input().split())
b = list(input().split())


for i in b :
    if i in d :
        d[i] += 1
    else :
        d[i] = 1

    
result = []

for data in a :
    if data not in d :
        result.append(data)
result.sort()


for res in result :
    print(res)
        