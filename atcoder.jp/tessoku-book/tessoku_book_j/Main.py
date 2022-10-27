n = int(input())
arr = list(map(int, input().split()))
d = int(input())
P = [0]*(n+1)
Q = [0]*(n+1)
for i in range(n):
    if i == 0:
        P[0] = arr[0]
    else:
        P[i] = max(P[i-1], arr[i])

for i in range(n-1, -1, -1):
    if i == n:
        Q[i] = arr[i]
    else:
        Q[i] = max(Q[i+1], arr[i])

for i in range(d):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(max(P[l-1], Q[r+1]))