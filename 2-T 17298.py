from collections import deque
n = int(input())
arr = list(map(int,input().split()))
q = deque()
ret = [-1] * n  # Initialize the ret list with -1


answer = [-1] * n
stack = []


stack.append(0)
for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)


print(*answer)
    
    