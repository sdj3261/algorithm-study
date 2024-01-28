def get_apple(board,firstMove,secondMove,thirdMove) :
    #범위안에 들어가는지 확인하자
    if in_range(firstMove) == False or in_range(secondMove) == False :
        return 0
    #장애물로는 갈수없다.
    if board[firstMove[0]][firstMove[1]] == -1 or board[secondMove[0]][secondMove[1]] == -1 :
        return 0

    apple_num = board[firstMove[0]][firstMove[1]] + board[secondMove[0]][secondMove[1]]

    if in_range(thirdMove) and board[thirdMove[0]][thirdMove[1]] == 1 :
        apple_num += 1
    return apple_num

def in_range(board) :
    if board[0] < 0 or board[0] > 4 or board[1] < 0 or board[1] > 4 :
        return False
        
board = [[0] * 5 for _ in range(5)]
dd = [(-1,0),(0,1),(1,0),(0,-1)]

for i in range(5) :
    board[i] = list(map(int,input().split()))
r,c = map(int,input().split())

appleCnt = False

for i in range(4) :
    for j in range(4) : 
        for k in range(4) :
            #1번째 이동
            firstMove = [r + dd[i][0],c+dd[i][1]]
            secondMove = [firstMove[0] + dd[j][0],firstMove[1] + dd[j][1]]
            thirdMove = [secondMove[0] + dd[j][0],secondMove[1] + dd[j][1]]

            if get_apple(board,firstMove,secondMove,thirdMove) >= 2 :
                appleCnt = True

if appleCnt :
    print(1)
else : 
    print(0)

    
