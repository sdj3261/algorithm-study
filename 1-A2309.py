from itertools import combinations
arr = []
for i in range(9) :
    arr.append(int(input()))
arr.sort()
left = 0
right = 7
height_sum = sum(arr)
exclude_idx =[]
found = False
for i in range(8) :
    for j in range(i+1,9) :
        if height_sum - (arr[i] + arr[j]) == 100 :
            exclude_idx.append(i)
            exclude_idx.append(j)
            found = True
            break
    if found :
        break

for i in range(9) :
    if i not in exclude_idx:
        print(arr[i])



