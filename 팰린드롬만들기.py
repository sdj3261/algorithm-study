data =input()
m = dict()
odd_flag = 0
mid_data = ""

for i in data :
    if i not in m :
        m[i] = 1
    elif i in m :
        m[i] += 1

for k,v in m.items() :
    if v % 2 == 1 :
        mid_data = k
        odd_flag += 1

if len(data) == 0 :
    print("I'm Sorry Hansoo")
else :
    if odd_flag > 1 :
        print("I'm Sorry Hansoo")
    else :
        ret = ""
        for key in sorted(m.keys()) :
    
            ret += key * (m[key] // 2)
        temp_ret = ret[::-1]
        print(ret + mid_data + temp_ret)
        
            
            
        