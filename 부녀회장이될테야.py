#1층의 3호 살거면
#0층의 1호부터 3호사람들의 수만큼 다 합해야 살수있다. 계약조항

t = int(input())
apart = [[-1 for _ in range(15)] for _ in range(15)]
n = len(apart)
for i in range(n) :
    sumPrefix = []
    for j in range(1,n) :
        if i==0 :
            apart[i][j] = j
        else :
            apartSum = 0
            for k in range(1,n) :
                apartSum = apartSum + apart[i-1][k]
                apart[i][k] = apartSum

for i in range(t):
    k = int(input())
    n = int(input())
    print(apart[k][n])

