from collections import deque
n = int(input())
q = deque()
mx_stu = 0 
stu_no = 0


for i in range(n) :
    info = list(map(int,input().split()))
    if info[0] == 1 :
        q.append(info[1])
    elif info[0] == 2 :
        if q :
            q.popleft()
    if mx_stu <= len(q) :
        mx_stu = len(q)    
        stu_no = q[-1]

print(mx_stu, stu_no)

    