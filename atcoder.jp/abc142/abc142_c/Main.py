n = int(input())
ref = {}
arr = list(map(int, input().split()))
for i in range(1, n+1):
    ref[i] = arr[i-1]

ref = sorted(ref.items(), key=lambda ref: ref[1])
for key, val in ref:
    print(key, end=' ')
print()