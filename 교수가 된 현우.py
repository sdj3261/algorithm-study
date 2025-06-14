t = int(input())


for i in range(t) :
    data = int(input())
    fiveCount = 0
    n = 5
    divisor = 1
    while n*divisor <= data :
        fiveCount += data // (n * divisor)
        divisor *= 5
    print(fiveCount)

