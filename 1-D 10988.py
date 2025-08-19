a,b,c =  map(int,input().split())
time = [0] * 101
for i in range(3) :
    at, lt = map(int,input().split())
    for j in range(at, lt) :
        time[j] += 1

ret = 0
for i in range(len(time)) :
    if time[i] == 1 :
        ret += a
    elif time[i] == 2 :
        ret += (2 * b)
    elif time[i] ==3 :
        ret += (3 * c)
print(ret)

