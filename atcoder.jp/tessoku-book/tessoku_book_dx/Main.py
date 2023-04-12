from collections import deque

s = input()
que = deque()

for i in range(len(s)):
    if s[i] == '(':
        que.append(i+1)
    else:
        tmp = que.pop()
        print(tmp, i+1)
        