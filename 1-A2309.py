arr = []
arr_height = []
for i in range(9) :
    arr.append(int(input()))
sum_arr = sum(arr)
ex_arr = []

# 두번째 방법
for i in range(len(arr)) :
    for j in range(i+1,len(arr)) :
        if sum_arr - arr[i] - arr[j] == 100 :
            ex_arr.append(i)
            ex_arr.append(j)
            break
ret_arr = []

for i in range(len(arr)) :
    if i not in ex_arr :
        ret_arr.append(arr[i])
for height in sorted(ret_arr) :

        
            
# found = False

#첫번째 방법 combi 인덱스 2개 조합해서 100이되는걸 찾자!
# def combi(start, depth) :
#     global found
#     if found :
#         return
#     if depth == 7 :
#         if sum(arr_height) == 100 :
#             for height in sorted(arr_height) :
#                 print(height)
#             found = True
#         return
#     for i in range(start, 9) :
#         arr_height.append(arr[i])
#         combi(i+1, depth+1)
#         arr_height.pop()
# combi(0,0)

        
            