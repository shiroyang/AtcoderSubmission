d, n = map(int, input().split())
arr = [24]*(d+1)
arr[0] = 0

for i in range(n):
    l ,r, h = map(int, input().split())
    for j in range(l , r+1):
        arr[j] = min(arr[j], h)
print(sum(arr))