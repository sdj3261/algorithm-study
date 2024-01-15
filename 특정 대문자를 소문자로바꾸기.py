data = input()
skip = list(input().split())
d = dict()
for a in skip :
    if a.isupper() :
        d[a] = a.lower()

result = ""

for c in data :
    if c in d :
        result += d[c]
    else :
        result += c
print(result)
    
    