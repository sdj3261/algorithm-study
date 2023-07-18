n = int(input())
for i in range(n):
    check = True
    ps = []
    data = input()
    for gwalho in data:
        if gwalho == ')':
            if len(ps) > 0:
                ps.pop()
            else:
                check = False
                break
        else:
            ps.append(gwalho)
            
    if len(ps) == 0 and check:
        check = True
    elif check == False :
        pass
    else:
        check = False

    if check:
        print("YES\n")
    else:
        print("NO\n")
