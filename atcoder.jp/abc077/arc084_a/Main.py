from bisect import bisect_right, bisect_left
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
C.sort()
ans = 0
# [1, 2, 3, 4, 5, "6", 6, 6, 7, 8, 9] len=11
for item in B:
    pos1 = bisect_left(A, item)
    pos2 = bisect_right(C, item)
    rem = len(C) - pos2
    ans += pos1 * rem
print(ans)