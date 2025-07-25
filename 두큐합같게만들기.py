from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)


    mid = 0
    for i in queue1 :
        mid += i
    for i in queue2 :
        mid += i
    # 홀수면 절반이 안되므로 return
    if mid % 2 != 0:
        return -1

    mid = mid // 2

    s1,s2 = sum(q1), sum(q2)

    cnt = 0
    max_cnt = (len(q1) + len(q2)) * 2

    i,j = 0,0
    #queue 간 합 계산
    while cnt <= max_cnt :
        if s1 == mid :
            print(s1, s2, mid)
            return cnt
        elif s1 > mid  and q1 :
            val = q1.popleft()
            s1 -= val
            q2.append(val)
            s2 += val
        elif s2 > mid and q2 :
            val = q2.popleft()
            s2 -= val
            q1.append(val)
            s1 += val
        else :
            return -1
        cnt += 1
    return -1


print(solution([1,1],[4,6,5,1]))