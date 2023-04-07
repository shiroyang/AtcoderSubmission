N = int(input())
A = list(map(int, input().split()))

j = N-2
while A[j] < A[j+1]:
    j -= 1
k = N-1
while A[k] > A[j]:
    k -= 1
    
A[k], A[j] = A[j], A[k]
print(*A[:j+1], *reversed(A[j+1:]))