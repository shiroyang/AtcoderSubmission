N, Q = map(int, input().split())
A = [list(map(int, input().split()))[1:] for _ in range(N)]

for _ in range(Q):
    s, t = map(lambda x: int(x)-1, input().split())
    print(A[s][t])