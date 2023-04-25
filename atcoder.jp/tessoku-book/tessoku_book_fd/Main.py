N = int(input())
print(N)
A = [N] + [i for i in range(1, N+1)]

for i in range(len(A)-1):
    print(A[i], A[i+1])