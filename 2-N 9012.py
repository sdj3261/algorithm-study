from collections import deque
q = deque()
n = int(input())
datas = []

for i in range(n) :
    datas.append(input())


for data in datas :
    q = deque()
    #q에 포인터넣기
    q.append(data[0])
    ptr = 1
    while ptr < len(data) :
        q.append(data[ptr])

        if len(q) > 1 :
            beforeData = q[-2]
            # () 모양일때 popleft
            if data[ptr] == ')' and beforeData == '(' :
                q.pop()
                q.pop()
        ptr += 1
    #q 초기화
    if len(q) == 0 :
        print("YES")
    else :
        print("NO")




