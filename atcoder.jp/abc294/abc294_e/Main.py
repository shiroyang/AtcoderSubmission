from sys import stdin
from collections import deque
input=lambda :stdin.readline()[:-1]

_, n1, n2 = map(int, input().split())
l = deque()
r = deque()

for _ in range(n1):
    num, cnt = map(int, input().split())
    l.append((num, cnt))
    
for _ in range(n2):
    num, cnt = map(int, input().split())
    r.append((num, cnt))

ans = 0
while len(l) > 0:
    l_num, l_cnt = l.popleft()
    r_num, r_cnt = r.popleft()
    if l_num == r_num:
        if l_cnt <= r_cnt:
            r_cnt -= l_cnt
            ans += l_cnt
            r.appendleft((r_num, r_cnt))
        else:
            l_cnt -= r_cnt
            ans += r_cnt
            l.appendleft((l_num, l_cnt))  
    else:
        if l_cnt <= r_cnt:
            r.appendleft((r_num, r_cnt-l_cnt))
        else:
            l.appendleft((l_num, l_cnt-r_cnt))

print(ans)