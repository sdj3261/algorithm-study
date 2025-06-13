n = int(input())
inputs = list(map(int, input().split()))
stk = []
ret = [-1] * n

for i in range(len(inputs)):
    while stk and inputs[stk[-1]] < inputs[i]:
        ret[stk.pop()] = inputs[i]
    stk.append(i)

print(*ret)
