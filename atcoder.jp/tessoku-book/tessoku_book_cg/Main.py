# 二次元累積和、
# 1-index
from sys import stdin
input = stdin.readline

Const = 1500
N = int(input())
S = [[0]*(Const+1) for _ in range(Const+1)]
T = [[0]*(Const+1) for _ in range(Const+1)]

def calc(a, b, c, d):
    return T[c][d] + T[a-1][b-1] - T[c][b-1] - T[a-1][d]

for _ in range(N):
    x, y = map(int, input().split())
    S[x][y] += 1

# 二次元累積和を一度のループで更新する
for i in range(1, Const+1):
    for j in range(1, Const+1):
        T[i][j] = T[i-1][j] + T[i][j-1] - T[i-1][j-1] + S[i][j]

q = int(input())
for _ in range(q):
    a, b, c, d = map(int, input().split())
    print(calc(a, b, c, d))