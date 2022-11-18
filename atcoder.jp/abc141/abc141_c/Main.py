# O(n)で実現する必要がある
n, k, q = map(int, input().split())
arr = [k-q]*(n+1)
for _ in range(q):
    c = int(input())
    arr[c] += 1
for i in range(1, n+1):
    if arr[i] > 0:
        print("Yes")
    else:
        print("No")