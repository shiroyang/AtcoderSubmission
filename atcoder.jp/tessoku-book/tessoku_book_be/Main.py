# Doubling
# catupper様の写経

N, Q = map(int, input().split())
A = [0] + list(map(int, input().split()))

N += 1

# 2^32 > 10**9
nxt = [[0]*32 for _ in range(N)]
# 1->2->4->8 ...
for rank in range(32):
    for i in range(N):
        if rank == 0:
            nxt[i][rank] = A[i]
        else:
            nxt[i][rank] = nxt[nxt[i][rank-1]][rank-1]

#  大きい桁から遷移
def calc(x, y):
    for i in range(31, -1, -1):
        # 左から見て、引けたらすぐ引く、そして遷移
        if y >= (1<<i):
            x = nxt[x][i]
            y -= 1 << i
    
    return x

for _ in range(Q):
    x, y = map(int, input().split())
    print(calc(x, y))