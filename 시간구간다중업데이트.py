def translateTimeString(data):
    mm = data[0:2]
    ss = data[3:5]
    return int(mm) * 60 + int(ss)

n = int(input())  
time_counts = [0] * 3600

for _ in range(n):
    parts = input().split() 
    select = int(parts[0])

    if select == 1:
        start_time, end_time = parts[1], parts[2]
        for i in range(translateTimeString(start_time), translateTimeString(end_time)):
            time_counts[i] += 1
    elif select == 2:
        start_time = parts[1]
        timeSec = translateTimeString(start_time)
        print(time_counts[timeSec])
