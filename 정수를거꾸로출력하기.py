num = input()
a = []
for i in range(len(num)-1,-1,-1) :
    a.append(num[i])
answer = ""
for i in a :
    if len(answer) == 0 and i == '0' or i == 0 :
        continue
    answer += i
print(answer)