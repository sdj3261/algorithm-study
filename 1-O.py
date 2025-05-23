from collections import deque

q = deque()

def find_answer(n):
    visited = set()
    q.append(('1', 1 % n))
    visited.add(1 % n)

    while q:
        num_str, mod = q.popleft()
        if mod == 0:
            return len(num_str)
        next_mod = (mod * 10 + 1) % n
        visited.add(next_mod)
        q.append((num_str + '1', next_mod))
    
    

while True:
    a = int(input())
    if a == 0:
        break
    print(find_answer(a))
