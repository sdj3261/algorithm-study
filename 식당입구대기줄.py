from collections import deque
n = int(input())
q = deque()
answer = [0,0]


infos = list(list(map(int,input().split())) for _ in range(n))
for info in infos :
    if info[0] == 1 :
        q.append(info[1])
        stu_no = info[1]
        if answer[0] < len(q) :
            answer[0] = len(q) 
            answer[1] = info[1]
            if info[1] < answer[1] and answer[0] == len(q):
                answer[1] = info[1]
    elif info[0] == 2 :
        if q :
            q.popleft()


print(answer[0], answer[1])

    