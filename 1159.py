num = int(input())
m = dict()
check = []
for i in range(num) :
    name = input()
    if name[0] in m :
        m[name[0]] += 1
    else :
        m[name[0]] = 1
for k,v in m.items() :
    if v >= 5 :
        check.append(k)

if len(check) == 0 :
    print("PREDAJA")
else :
    print("".join(sorted(check)))

    