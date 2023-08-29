n,c = map(int,input().split())
dict = {}
num = map(int,input().split())

for i in num :
    if i not in dict :
        dict[i] = 1
    else :
        dict[i] += 1

sortedDict = sorted(dict.items(),key=lambda x : -x[1])
print(sortedDict)

for key,value in sortedDict :
    for j in range(value) :
        print(key, end = " ")

    