from collections import deque
def solution(S):
    #Early return
    if len(S) == 1:
        return S
    #큐에다가 담으면서 9보다 작거나 같으면 합친다
    q = deque()

    for ch in S:
        num = int(ch) #현재 인덱스 값 체킹
        # q에 값이 있을때부터 검사 후 합칠지 말지 결정
        if q and q[-1] + num <= 9:
            q[-1] += num
        else:
            q.append(num)
    return ''.join(map(str, q))
