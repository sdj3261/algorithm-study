ret = []
while True :
    line = input()
    ps = []
    ans = True
    if line == '.' :
        break
    for i in line :
        if i == ')' :
            if ps and ps[-1] == '(' :
                ps.pop()
            else :
                ans = False
                break
        elif i == ']' :
            if ps and ps[-1] == '[' :
                ps.pop()
            else :
                ans = False
                break
        
        elif i == '(' or i== '[' :
            ps.append(i)
        
                

    if len(ps) == 0  and ans :
        ret.append("yes")
    else :
        ret.append("no")
for j in ret :
    print(j, end="\n")

    
            
    