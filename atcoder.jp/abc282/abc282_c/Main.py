from collections import deque
n = int(input())
s = input()
que = deque()
flag = False

for i in range(n):
    if not flag:
        if 'a' <= s[i] <= 'z':
            print(s[i], end='') 
        elif s[i] == ',':
            print('.', end= '')
        elif s[i] == '"':
            print('"', end='')
            flag = True
    else:
        if 'a' <= s[i] <= 'z':
            print(s[i], end='')
        elif s[i] == ',':
            print(',', end= '')
        elif s[i] == '"':
            print('"', end='')
            flag = False
print()