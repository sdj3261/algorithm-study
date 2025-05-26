from collections import deque
num = int(input())
ret = 0
q = deque()

for i in range(num) :
    data = input()
    for j in data :
        if q and q[-1] == j :
            q.pop()
            continue
        q.append(j)
    if len(q) == 0 :
        ret+=1
    else :
        q.clear()
print(ret)
            
        
        
        
        

# num = int(input())
# m = int(input())
# data = list(map(int,input().split()))
# ret = 0
# result = []
# combi = []

# def dfs(start):
#     global ret
#     if len(combi) == 2:
#         if data[combi[0]] + data[combi[1]] == m :
#             ret += 1
#         return
#     for i in range(start, len(data)):
#         combi.append(i)
#         dfs(i + 1)
#         combi.pop()

# dfs(0)    
    

# print(ret)