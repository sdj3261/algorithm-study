from collections import deque
n = int(input())
arr = list(map(int,input().split()))
ret = []
tmp = []
for idx in range(1,n) :
    if arr[idx] > arr[idx-1] :
        ret.append(arr[idx])
    else 
    