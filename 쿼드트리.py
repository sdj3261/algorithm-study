n = int(input())
board = [[0] * n for _ in range(n)]

for i in range(8) :
    data = input()
    for j in range(8) :
        board[i][j] = int(data[j])
        
def quadtree(y,x,depth) :
    #기저 조건
    if depth == 1 :
        return board[y][x]
    # 그외에 어떤로직을 세워야할까? 4분의1로 쪼갠 후 모두 같은지 확인 다르면 계속 쪼개기 아니면 pass
    # 0과 1일이 섞여서 한번에 나타내지 못하는 경우 -> 4개로 나누어 압축하고 사분면 결과를 괄호 안에 묶는다.
    # 즉 0과 1일이 섞이지 않는 경우 -> 괄호없이 쓴다.
    else :
        ret = []
        ret.append(quadtree(y,x,depth//2))
        ret.append(quadtree(y,x+depth//2,depth//2))
        ret.append(quadtree(y+depth//2,x,depth//2))
        ret.append(quadtree(y+depth//2,x+depth//2,depth//2))
        if ret[0] == ret[1] == ret[2] == ret[3] :
            return ret[0]
        else :
            return "(" + "".join(map(str,ret)) + ")"
print(quadtree(0,0,n))