def solution(video_len, pos, op_start, op_end, commands):
    def prev_move(pos1):
        pos1 = op_check(pos1)
        if pos1 <= 10:
            pos1 = 0
        else:
            pos1 = pos1 - 10
        pos1 = op_check(pos1)
        return pos1

    def next_move(pos1):
        pos1 = op_check(pos1)
        second_viedo_len = change_second(video_len)
        if pos1 + 10 >= second_viedo_len:
            pos1 = second_viedo_len
        else:
            pos1 = pos1 + 10
        pos1 = op_check(pos1)
        return pos1

    def op_check(pos1):
        ops_second = change_second(op_start)
        ope_second = change_second(op_end)
        if ops_second <= pos1 <= ope_second:
            return ope_second
        return pos1

    def change_second(data):
        ret = 0
        arr = data.split(':')
        ret += int(arr[0]) * 60
        ret += int(arr[1])
        return ret

    def change_str(data):

        minute = data // 60
        second = data % 60
        str_minute = str(minute)
        str_second = str(second)

        if len(str_minute) == 1:
            str_minute = "0" + str_minute
        if len(str_second) == 1:
            str_second = "0" + str_second
        return str_minute + ":" + str_second

    current_pos = change_second(pos)
    for command in commands:
        if command == "next":
            current_pos = next_move(current_pos)
        elif command == "prev":
            current_pos = prev_move(current_pos)
        else:
            pass

    return change_str(current_pos)
# 10초 전 이동 "prev" 10초미만 처음위치 이동 0분0초
# 10초 후 next 10초 후 이동 10초 미만인경우 마지막 위치 동영상길이
# 현재 재생위치 op_start opend 오프닝 끝나는 위치로 이도ㅓㅇ

# 입력 종료 후 영상 위치 mm:ss로 이동
