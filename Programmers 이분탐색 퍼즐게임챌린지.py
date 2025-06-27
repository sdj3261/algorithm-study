def solution(diffs, times, limit):
    n = len(diffs)
    ret = 0
    left = 1
    right = max(diffs)
    arr = []

    while left <= right:
        level = (right + left) // 2
        sub_ret = 0
        for i in range(n):
            retryCount = diffs[i] - level
            if retryCount > 0:
                sub_ret += retryCount * (times[i] + times[i - 1]) + times[i]
            else:
                sub_ret += times[i]
        if limit >= sub_ret:
            right = level - 1
            arr.append(level)
        else:
            left = level + 1

    return min(arr)
