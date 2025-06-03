n = int(input())
times = []

one_win_time = 0
two_win_time = 0
total_game_time = 60 * 48
one_win_check = True
one_score = 0
two_score = 0

def timeToMinutes(time) :
    minute,second = time.split(':')
    minute = int(minute)
    second = int(second)
    return minute * 60 + second

for i in range(n) :
    win_team, time = input().split()
    times.append((int(win_team),timeToMinutes(time)))

#초기 세팅 시작
win_team, time = times[0]
if win_team == 1 :
    one_score+=1
else :
    two_score+=1

for i in range(1,n+1) :
    #이전 시간 가져온다.
    win_team, time = times[i-1]
    #i가 마지막값이 아닌지 비교한다.
    if i != n :
        new_win_team, newTime = times[i]
    else :
        new_win_team = 0
        newTime = total_game_time

    #승리한 시간은 새로운시간 , 마지막 총게임시간 - 이전시간으로 계산한다.
    winning_time = newTime - time
    # 2번째 인덱스부터 시작하므로 기존 이기고 있던 시간을 마지막게임시간, 그다음시간에서 뺴준다.
    if one_score > two_score :
        one_win_time += winning_time
    elif two_score > one_score :
        two_win_time += winning_time

    #점수 기록을 갱신한다.     유리한경우만 체크
    if new_win_team == 1:
        one_score += 1
    else:
        two_score += 1


def secondToTime(second) :
    min, sec = divmod(second, 60)
    strMin = ""
    strSec = ""
    if min < 10 :
        strMin =  "0" + str(min)
    else :
        strMin = str(min)
    if sec < 10 :
        strSec = "0" + str(sec)
    else :
        strSec = str(sec)
    return strMin + ":" + strSec

print(secondToTime(one_win_time))
print(secondToTime(two_win_time))







