N, M = map(int, input().split())
G = [[False]*(N) for _ in range(N)]
for i in range(N):
    G[i][i] = True

for _ in range(M):
    A = list(map(lambda x: int(x)-1, input().split()))[1:]
    for i in range(len(A) - 1):
        for j in range(i+1, len(A)):
            G[A[i]][A[j]] = True
            G[A[j]][A[i]] = True

for li in G:
    for item in li:
        if item == False:
            exit(print("No"))
print("Yes")