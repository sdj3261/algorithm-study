def solve(a) :
    if a == 1 :
        return 1
    else :
        return a + solve(a-1)
a = int(input())
print(solve(a))
    