from collections import deque

while True:
    data = input()
    if data == '.':
        break
    q = deque()
    exitFlag = False
    for i in data:
        if i == '(' or i == '[':
            q.append(i)
        elif i == ')':
            if q and q[-1] == '(':
                q.pop()
            else:
                exitFlag = True
                break
        elif i == ']':
            if q and q[-1] == '[':
                q.pop()
            else:
                exitFlag = True
                break
    if exitFlag or q:
        print("no")
    else:
        print("yes")
