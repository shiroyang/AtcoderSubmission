# dp with restoration
# dp[i][j]: prev i, reaching j, doable or not
# Tabel[i][j] -> Table[i-1][j-A[Table[i][j]]]

CON = 10000
n, s = map(int, input().split())
A = list(map(int, input().split()))

dp = [[False]*(CON+1) for _ in range(n+1)]
dp[0][0] = True
Table = [[0]*(CON+1) for _ in range(n+1)]

for i in range(n):
    for j in range(CON+1):
        if dp[i][j]:
            dp[i+1][j] = True
            if A[i] + j < CON+1:
                dp[i+1][j+A[i]] = True
                Table[i+1][j+A[i]] = i+1


path = []
i = n
while i >= 0:
    if Table[i][s] != 0:
        path.append(Table[i][s])
        s -= A[Table[i][s]-1]
    i -= 1
path = path[::-1]
if path:
    print(len(path))
    print(*path)
else:
    print(-1)