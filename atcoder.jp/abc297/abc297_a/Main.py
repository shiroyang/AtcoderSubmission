ans = -1

n, d = map(int, input().split())
A = list(map(int, input().split()))
for i in range(1, n):
    if A[i] - A[i-1] <= d:
        print(A[i])
        exit()
        
print(ans)