n = int(input())
# 연속된 숫자 찾기
# 앞에 0이면 삭제 필요
arr = []
datas = []
def compactNumber(data) :
    ret = data
    while True :
        if len(ret) >= 2 and ret[0] == '0' :
            ret = ret[1:]
        else :
            return int(ret)

for i in range(n) :
    data =str(input())
    datas.append(data)

for i in datas :
    subSeq = ""
    for j in i :
        if j.isdigit() :
            subSeq = subSeq + j
        else :
            if len(subSeq) != 0 :
                arr.append(compactNumber(subSeq))
                subSeq = ""
            pass
    if len(subSeq) > 0 :
        arr.append(compactNumber(subSeq))
        subSeq = ""

for i in sorted(arr) :
    print(i)


