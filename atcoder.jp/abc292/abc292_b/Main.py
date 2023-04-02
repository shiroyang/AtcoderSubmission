n, q = map(int, input().split())
A = [0]*(n+1)
for _ in range(q):
    idx, x = map(int, input().split())
    if idx == 1:
        A[x] += 1
    elif idx == 2:
        A[x] += 2
    elif idx == 3:
        if A[x] >= 2:
            print("Yes")
        else:
            print("No")