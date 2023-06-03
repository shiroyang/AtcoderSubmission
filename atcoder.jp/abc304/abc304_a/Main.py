n = int(input())
A = []
B = []

for _ in range(n):
    a, b = input().split()
    A.append(a)
    B.append(int(b))
    
MI = 10**9
idx = 0

for i in range(n):
    if B[i] < MI:
        idx = i
        MI = B[i]

for i in range(idx, n):
    print(A[i])

for i in range(idx):
    print(A[i])
