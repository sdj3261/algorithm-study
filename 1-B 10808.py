cnt = [0] * 26
data = input()
for c in data :
    cnt[ord(c) - ord('a')] += 1
print(*cnt)