a, b, k = map(int, input().split())
arr = []

for i in range(1, min(a, b)+1):
    if a % i == 0 and b % i == 0:
        arr.append(i)
arr.reverse()
print(arr[k-1])
