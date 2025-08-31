n = int(input())
nl = list(map(int,input().split()))
m = int(input())
ml = list(map(int,input().split()))
d = dict()
for i in nl :
    if i not in d :
        d[i] = 0
    else : 
        d[i] += 1
answer = []
for j in ml :
    if j in d :
        answer.append(d[j])
    else :
        answer.append(0)
d = dict()

print(*answer)