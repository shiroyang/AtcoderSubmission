n = int(input())
arr = list(map(int, input().split()))
ref = set(range(1, n+1))
for idx, ele in enumerate(arr, 1):
    if idx in ref:
        if ele in ref:
            ref.discard(ele)
ans = sorted(list(ref))
print(len(ans))
print(*ans, sep=' ')