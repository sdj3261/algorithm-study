n = int(input())
arr = list(map(int,input().split()))
d = dict()
mx = 0 
for i in arr :
    if i in d :
        d[i] += 1
    else :
        d[i] = 1
    mx = max(mx,d[i])

answer = []
for k,v in d.items() :
    if mx == v :
        answer.append(k)

answer.sort()
for i in answer :
    print(i, end= ' ')
    
        
    
