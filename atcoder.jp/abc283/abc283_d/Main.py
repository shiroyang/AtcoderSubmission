# stackの中にsetを保存する
from collections import deque

s = input()
used = set()
que = deque()
subset = set()

for letter in s:
    if letter == '(':
        subset = set()
        que.append(subset)
    elif letter == ')':
        if len(que) > 0:
            tmp = que.pop()
            for ele in tmp:
                used.discard(ele)
    else:
        if letter in used:
            print("No")
            exit()
        else:
            used.add(letter)
            if len(que) > 0:
                tmp = que.pop()
                tmp.add(letter)
                que.append(tmp)
print("Yes")