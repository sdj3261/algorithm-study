import math

a, b, v = map(int, input().split())

# (v-a)까지 올라가는 데 필요한 일수
days = math.ceil((v - a) / (a - b)) + 1
print(days)
