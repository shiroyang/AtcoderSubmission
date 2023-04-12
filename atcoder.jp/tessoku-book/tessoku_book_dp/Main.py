# 各生徒の間違った回数だけを記録する
N, M = map(int, input().split())
G = [0]*(N+1)

A = list(map(int, input().split()))

for item in A:
    G[item] += 1
    
for i in range(1, N+1):
    print(M-G[i])