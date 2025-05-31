n = int(input())
board =[[0] * n for i in range(n)]
for i in range(n) :
    data = input()
    for j in range(n) :
        board[i][j] = int(data[j])
def quadTree(y,x,n) :
    if n == 1 :
        return board[y][x]
    ret = []

quadTree(0,0,n)

