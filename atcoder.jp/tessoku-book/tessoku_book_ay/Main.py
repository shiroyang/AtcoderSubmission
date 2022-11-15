from collections import deque

que = deque()
n = int(input())
for i in range(n):
    s = input()
    if s[0] == '1':
        num ,name = s.split()
        num = int(num)
        que.append(name)
    elif s[0] == '2':
        print(que[-1])
    elif s[0] == '3':
        que.pop()
