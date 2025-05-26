n, k = map(int,input().split())
data = list(map(int, input().split()))
p_sum = []
ret = float('-inf')  # 아주 작은 값으로 초기화
init_data = 0
for i in range(0,k) :
    init_data += data[i]
p_sum.append(init_data) #초기값 세팅
cnt = 0 
for i in range(k,len(data)) :
    sums = 0
    sums += p_sum[cnt] + data[i] - data[cnt]
    cnt+=1
    p_sum.append(sums)

for i in range(len(p_sum)) :
    ret = max(ret,p_sum[i]) 
print(ret)
    

    
    