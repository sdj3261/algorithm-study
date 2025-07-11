n = int(input())
arr = list(map(int, input().split()))
path = []
ret_s = 10000000000
# 순열 순서바꿔서도 계산해서 최소값 구하기
# 순열 is S not in path
# 콤비 is S

def countAttack(path):
    count = 0
    newScv = []
    for scv in path:
        newScv.append(arr[scv])
    while len(newScv) != 0:
        dmg = 9
        offset = 1
        for i in range(len(newScv)):

            newScv[i] = newScv[i] - dmg // offset
            offset *= 3

        # 0 이하 제거
        newScv = [hp for hp in newScv if hp > 0]

        count += 1
    return count
#dd
# def permu() :
#     if len(path) == len(arr) :
#         print(*path)
#         return
#     for i in range(len(arr)):
#         if arr[i] not in path :
#             path.append(arr[i])
#             permu()
#             path.pop()
# permu()

def dfs():
    global ret_s
    if len(path) == len(arr):
        ret_s = min(ret_s, countAttack(path))
        return
    for i in range(len(arr)):
        if i not in path: # 이거 뺴면 중복순열 arr[i]가 들어왔는지 체크한다
            path.append(i)
            dfs()
            path.pop()

dfs()
print(ret_s)
