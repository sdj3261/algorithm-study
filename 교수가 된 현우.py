t = int(input())

for _ in range(t):
    n = int(input())
    count = 0
    i = 5
    while n // i: # n의 5의 약수를 구하자
        count += n // i
        i *= 5 # 5가 2번곱해졌을수도 있으므로 25 ,125 이런것도 다 구해주자
    print(count) #