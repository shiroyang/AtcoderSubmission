from collections import deque, defaultdict
from functools import lru_cache


@lru_cache(maxsize=10**6)
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    pending_list = defaultdict(list)
    ans = deque()
    flag = False
    tmp = 0
    for _ in range(q):
        s = input()
        if s[0] == '1':
            idx, num = map(int, s.split())
            pending_list = defaultdict(list)
            flag = True
            tmp = num
            # arr = [num]*n
        if s[0] == '2':
            idx, a, b = map(int, s.split())
            pending_list[a].append(b)
            # arr[a-1] += b
        if s[0] == '3':
            if not flag:
                idx, num = map(int, s.split())
                arr[num-1] += sum(pending_list[num])
                pending_list[num].clear()
                ans.append(arr[num-1])
            if flag:
                idx, num = map(int, s.split())
                ans.append(tmp + sum(pending_list[num]))

    while len(ans) > 0:
        print(ans.popleft())

solve()