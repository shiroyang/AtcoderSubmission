n = int(input())
A = list(map(int, input().split()))

for i in range(len(A)-1):
    if A[i] - A[i+1] >= 1:
        for j in range(A[i], A[i+1], -1):
            print(j, end=' ')
    elif A[i+1] - A[i] >= 1:
        for j in range(A[i], A[i+1]):
            print(j, end=' ')
print(A[n-1])