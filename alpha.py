data = input()
alpha_cnt = [0] * 26
for i in data :
    alpha_cnt[ord(i)-ord('a')] += 1
for j in range(26) :
    print(alpha_cnt[j], end=" ")