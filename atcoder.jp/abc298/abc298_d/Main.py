'''
7
1 2
1 4
1 7
2
1 3
1 8
2

'''
from collections import deque
from sys import stdin
input = lambda: stdin.readline()[:-1]

MOD = 998244353
ans = 1
length = 1
que = deque()
que.append(1)

Q = int(input())
for _ in range(Q):
    li = list(map(int, input().split()))
    if li[0] == 1:
        que.append(li[1])
        ans = (ans * 10 + li[1]) % MOD
        length += 1
        
    elif li[0] == 2:
        length -= 1
        sentou = que.popleft()
        ans = (ans - (sentou * pow(10, length, MOD)))%MOD
        if ans < 0:
            ans += MOD
        
        
    elif li[0] == 3:
        ans = ans % MOD
        print(ans)