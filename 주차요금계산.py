from collections import deque


def toMinute(time):
    data = time.split(":")
    return int(data[0]) * 60 + int(data[1])

def solution(fees, records):
    defaultTime, defaultFee, unitTime, unitFee = fees
    park_in = dict()
    ret = dict()
    q = deque()
    #in 은 map으로 넣고
    #순회하면서 out발견 시 map에서 찾아 매칭 후 최종 결과 map에 박는다.

    for record in records:
        time, carNum, inOut = record.split(" ")
        if inOut == 'IN' :
            park_in[carNum] = time
        #OUT시 누적 주차 시간 계산
        elif inOut == 'OUT' :
            parkingTime = toMinute(time) - toMinute(park_in[carNum])
            if carNum in ret :
                ret[carNum] += parkingTime
            else :
                ret[carNum] = parkingTime
            park_in.pop(carNum)

    for k, v in park_in.items():
        parkingTime = toMinute('23:59') - toMinute(v)
        if k in ret:
            ret[k] += parkingTime
        else:
            ret[k] = parkingTime
    #누적시간에 따른 요금 계산
    #차번호, 누적시간
    for k, v in ret.items():
        mod = (v - defaultTime) % unitTime
        checkTime = (v - defaultTime) // unitTime
        if v <= defaultTime :
            ret[k] = defaultFee #defaultFee
        else :
            ret[k] = defaultFee + checkTime * unitFee
            #만약 mod 존재시 유닛fee 추가계산
            if mod :
                ret[k] = ret[k] + unitFee

    answer = []
    for k,v in sorted(ret.items()) :
        answer.append(v)

    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))