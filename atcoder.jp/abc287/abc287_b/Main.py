n, m = map(int, input().split())
A = [int(input()) for _ in range(n)]
B = set(int(input()) for _ in range(m))

cnt = 0
for item in A:
    tmp = item % 1000
    if tmp in B:
        cnt += 1
print(cnt)