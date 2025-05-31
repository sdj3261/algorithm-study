    # a,e,i,o,u 중 반드 시 하나 포함 체크
    # 모음이 3개 자음이 3개 연속으로 오면 false
    # 같은 글자 연속적으로 두번 오면 안되나 ee랑 oo만 허용
def check1(data) :
    if data.find('a') != -1 or data.find('e') != -1 or data.find('i') != -1 or data.find('o') != -1 or data.find('u') != -1 :
        return True
    else :
        return False

def check2(data) :
    moumCnt = 0
    zaumCnt = 0
    for i in range(len(data)) :
        # 모음체크하는함수
        if check1(data[i]) :
            moumCnt += 1
            zaumCnt = 0
        else :
            zaumCnt += 1
            moumCnt = 0
        if zaumCnt == 3 or moumCnt == 3 :
            return False
    return True

def check3(data) :
    for i in range(1,len(data)) :
        pos = data[i-1]
        if data[i] == 'o' or data[i] == 'e' :
            continue
        if pos == data[i] :
            return False
    return True


while True :
    data = input()
    if data == 'end' :
        break
    print("<" + data + ">" + " is", end = ' ')

    if check1(data) and check2(data) and check3(data) :
        print("acceptable.")
    else :
        print("not acceptable.")

