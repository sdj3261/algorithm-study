import sys
sys.setrecursionlimit(1000000)
n , m = map(int,input().split())
arr = [[0] * n for _ in range(n)]

selected_idx = []
chicken = []
house = []
ret = sys.maxsize
#집과 치킨집 사이의 최단거리의 합이 가장 작게되는 프로그램
for i in range(n) :
    data = list(map(int,input().split()))
    for j in range(n) :
        if data[j] == 2 :
            chicken.append((i,j))
        elif data[j] == 1 :
            house.append((i,j))
        arr[i][j] = data[j]

#치킨 인덱스의 콤비네이션 구하기
#콤비네션과 집들 사이의 최단거리 계산
def combi(idx_arr, start):
    if len(idx_arr) == m:
        selected_idx.append(idx_arr[:])
        return

    for i in range(start, len(chicken)):
        idx_arr.append(i)
        combi(idx_arr, i + 1)
        idx_arr.pop()

combi([], 0)


def compute_chicken_distance(house, chicken_s) :
    dist = sys.maxsize
    r1,c1 = house
    for chicken in chicken_s :
        dist = min(dist,abs(r1-chicken[0]) + abs(c1-chicken[1]))
    return dist


for selected in selected_idx :
    sum_s = 0
    chicken_s_data = []
    for k in selected :
        chicken_s_data.append(chicken[k])
    for h in house:
        sum_s += compute_chicken_distance(h, chicken_s_data)
    ret = min(ret, sum_s)
print(ret)








