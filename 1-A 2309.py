from itertools import combinations
arr = [0] * 9
for i in range(9) :
    arr[i] = int(input())
seven = list(combinations(arr,7))
for data in seven :
    if sum(data) == 100 :
        sorted_data = sorted(data)
        for i in sorted_data :
            print(i)
        break

