n = int(input())
arr = list(map(int, input().split()))

print(arr[0], end=' ')
for i in range(n-1):
    print(arr[i+1]-arr[i], end=' ')
print()