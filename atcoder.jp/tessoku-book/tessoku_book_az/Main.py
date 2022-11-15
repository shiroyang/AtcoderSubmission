from collections import deque
n = int(input())
que = deque()

for i in range(n):
    s = input()
    if s[0] == '1':
        idx, name = s.split()
        que.append(name)
    elif s[0] == '2':
        print(que[0])
    else:
        que.popleft()