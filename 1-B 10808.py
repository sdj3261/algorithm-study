cnt = [0] * 26
data = input()

for i in data :
    cnt[ord(i)-ord('a')] += 1

for i in range(26) :
    print(cnt[i], end=' ')