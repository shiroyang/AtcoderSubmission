h, w = map(int, input().split())
# input has no space, have to split 
mat = []
for i in range(h):
    s = input()
    arr = []
    for letter in s:
        arr.append(letter)
    mat.append(arr)

dp = [[0]*w for _ in range(h)]
dp[0][0] = 1

for i in range(h):
    for j in range(w):
        if i+j != 0:
            if mat[i][j] != '#':
                if i != 0 and j != 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                elif i != 0:
                    dp[i][j] = dp[i-1][j]
                elif j != 0:
                    dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = 0
                
print(dp[-1][-1])
                
