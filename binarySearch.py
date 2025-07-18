#N개의 집이 수직선 위에 있다.
# 이 집들 중 일부에 공유기를 설치하려 한다.
# 한 집에는 하나의 공유기만 설치할 수 있고,
# 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 C개의 공유기를 설치하려 한다.
# 최대 인접 거리의 최댓값을 구하라.

n= int(input())
nums = list(map(int,input().split()))
find_num = int(input())

left = 0
right = len(nums)-1
ret = -1
# 배열이 정렬되어있는 경우 해당 구간의 중앙값과 비교해서 왼쪽/오른쪽 절반 중 하나만 보면 된다”는 규칙이다.
while left <= right:# 0과 6 index 기준으로 설계
    mid = (left + right) // 2

    if nums[mid] == find_num:
        ret = mid
        break
    elif nums[mid] > find_num :
        right = mid-1
    else :
        left = mid+1
    print(left,right)
print(ret)

def binary_search(arr, fn, l, r) :
    if l > r:
        return -1  # 종료 조건

    m = (left + right) // 2
    if arr[m] == fn :
        return m
    elif arr[m] < fn:
        return binary_search(arr, fn, m+1, r)
    elif arr[m] > fn :
        return binary_search(arr, fn, l, m-1)


print(binary_search(nums, find_num, 0, len(nums)-1))

