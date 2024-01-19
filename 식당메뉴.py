from collections import deque
n = int(input())
q = deque()
A = []
B = []
C = []
for i in range(n) :
    data = list(map(int,input().split()))
    if len(data) >= 3 :
        q.append((data[1], data[2]))
    else :
        menu = q.popleft()
        if data[1] == menu[1] :
            A.append(menu[0])
        elif data[1] != menu[1] :
            B.append(menu[0])

while len(q) >= 1 :
    menu = q.popleft()
    C.append(menu[0])

A.sort()
B.sort()
C.sort()

if len(A) == 0 :
    print("None")
else :
    print(*A)
if len(B) == 0 :
    print("None")
else :
    print(*B)
if len(C) == 0 :
    print("None")
else :
    print(*C)