def solution(bandage, health, attacks):
    # t초동안 붕대감기 1초마다 x 회복
    # t초 연속으로 붕대 감으면 y만큼 체력 추가회복
    # 기술을 쓰다가 공격당하면 기술취소, 다시 스킬 사용 연속 성공이 0으로 초기화
    # 캐릭터가 끝까지 생존할 수 있는지 체크
    t, x, y = bandage
    curHealth = health
    heal = 0
    death = False
    m = {}

    for attack in attacks:
        m[attack[0]] = attack[1]

    for time in range(attacks[0][0], attacks[len(attacks) - 1][0] + 1):
        if m.get(time) is None:
            heal += 1
            curHealth += x
            if curHealth > health:
                curHealth = health
        else:
            curHealth = curHealth - m[time]
            heal = 0
            if curHealth <= 0:
                death = True
        if heal == t:
            heal = 0
            curHealth = curHealth + y
            if curHealth > health:
                curHealth = health

    if death:
        return -1
    else:
        return curHealth


