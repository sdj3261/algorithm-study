def solution(schedules, timelogs, startday):
    def to_min(t: int) -> int:
        return (t // 100) * 60 + (t % 100)

    # 해당 주의 7일 요일이 평일인지 미리 계산 (True=평일)
    # 1=월, ..., 7=일
    is_weekday = [(((startday - 1 + d) % 7) + 1) <= 5 for d in range(7)]

    answer = 0
    for i, pref in enumerate(schedules):
        cutoff = to_min(pref) + 10  # 희망 시각 + 10분

        ok = True
        #test
        for d in range(7):
            if is_weekday[d] and to_min(timelogs[i][d]) > cutoff:
                ok = False
                break

        if ok:
            answer += 1

    return answer
