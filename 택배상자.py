from collections import deque
def solution(order):
    stack = []
    idx = 0
    n = len(order)

    for box in range(1,n+1) :
        stack.append(box)
        while stack and idx < n and stack[-1] == order[idx] :
            stack.pop()
            idx += 1
    return idx
print(solution([5,4,3,2,1]))
