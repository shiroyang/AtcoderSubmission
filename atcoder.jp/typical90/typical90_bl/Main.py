N, Q = map(int, input().split())
A = list(map(int, input().split()))
diff = []
l1_kyori = 0
for i in range(len(A)-1):
    diff.append(A[i+1] - A[i])
    l1_kyori += abs(A[i+1] - A[i])
    
for _ in range(Q):
    l ,r, v = map(int, input().split())
    l -= 1; r -= 1
    if l != 0:
        before = diff[l-1]
        diff[l-1] += v
        l1_kyori += abs(diff[l-1]) - abs(before)
    if r != N-1:
        before = diff[r]
        diff[r] -= v
        l1_kyori += abs(diff[r]) - abs(before)
    print(l1_kyori)