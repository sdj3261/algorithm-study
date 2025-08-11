def max_two_two_digit_sum_verbose(s):
    n = len(s)
    subRet = float('-inf')

    #subString 2개 조합 int형 변환
    twoDigitNumbers = []
    for i in range(n - 1):
        two = s[i:i+2]
        twoDigitNumbers.append(int(two))

    # 겹치는 값 중 최대값 만들기
    fragments = [0] * len(twoDigitNumbers)
    for i in range(len(twoDigitNumbers)):
        if twoDigitNumbers[i] > subRet:
            subRet = twoDigitNumbers[i]
        fragments[i] = subRet

    ans = float('-inf')

    # [0,2], [1,3] 겹치지않는 범위에서 최대값 체크
    for i in range(2, len(twoDigitNumbers)):
        left = fragments[i - 2]
        right = twoDigitNumbers[i]

        ans = max(ans, left + right)

    return ans
print(max_two_two_digit_sum_verbose('9999999999999999999999999999999999999999999999999999999999999999999999999999999999'))