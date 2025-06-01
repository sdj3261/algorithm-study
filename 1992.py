n = int(input())
board =[[0] * n for i in range(n)]
for i in range(n) :
    data = input()
    for j in range(n) :
        board[i][j] = int(data[j])

def quadTree(y,x,n) :
    ret = ""
    flag = True
    #기저조건
    if n == 1 :
        return str(board[y][x])

    for i in range(y,y+n) :
        for j in range(x,x+n) :
            if board[y][x] != board[i][j] :
                flag = False
    if flag :
        return str(board[y][x])
    else :
        ret += ('(')
        ret += (quadTree(y,x,n//2))
        ret += (quadTree(y,x+n//2,n//2))
        ret += (quadTree(y+n//2,x,n//2))
        ret += (quadTree(y+n//2,x+n//2,n//2))
        ret += (')')
    return ret





print("".join(quadTree(0,0,n)))

