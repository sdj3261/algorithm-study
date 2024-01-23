from itertools import permutations
data, num = input().split()
result = list(permutations(data,len(data)))
result.sort()
seq = []
for data in result : 
    seq.append("".join(data))
print(seq[int(num)-1])