a = int(input())
arr = [[0] * a for _ in range(a)]
for i in range(a) :
    data = input()
    for j in range(a) :
        arr[i][j] = int(data[j])

print(arr)

def dfs(x,y, size) :
    #사이즈 부터 체킹 해서
    #만약 for문 돌아서 같지않다면 분할 진행
    #분할하면 괄호 삽입
    if size == 1 :
        return str(arr[x][y])
    half = size//2
    isSame = True
    #1사분면
    for i in range(x, x+ size) :
        if not isSame :
            break
        for j in range(y, y+size) :
            if arr[x][y] != arr[i][j] :
                isSame = False
                break
    if isSame:
        return str(arr[x][y])
    half = size // 2
    return "(" \
        + dfs(x, y, half) \
        + dfs(x, y + half, half) \
        + dfs(x + half, y, half) \
        + dfs(x + half, y + half, half) \
        + ")"

print(dfs(0,0, a))








