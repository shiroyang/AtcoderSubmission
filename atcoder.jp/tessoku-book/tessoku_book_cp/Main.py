# dp with restoration
# need a table for the transition

n = int(input())
A = list(map(int, input().split()))
INF = 10**16
dp = [INF]*n
dp[0] = 0
dp[1] = abs(A[1] - A[0])
table = [0]*n
table[1] = 1

for i in range(2, n):
    if dp[i-1] + abs(A[i]-A[i-1]) < dp[i-2] + abs(A[i]-A[i-2]):
        table[i] = 1
        dp[i] = dp[i-1] + abs(A[i]-A[i-1])
    else:
        table[i] = 2
        dp[i] = dp[i-2] + abs(A[i]-A[i-2])

path = []
idx = n-1

while idx != 0:
    path.append(idx)
    idx = idx - table[idx]

path.append(0)
path = path[::-1]
print(len(path))
for v in path:
    print(v+1, end=' ')
print()