n, m = list(map(int,input().split()))
answer = 0
d = dict()
for i in range(n) :
    item, price = list(input().split())
    d[item] = price
    
buys = list(input().split())
for buy in buys :
    if buy in d.keys() :
        answer += int(d[buy])
        
print(answer)
