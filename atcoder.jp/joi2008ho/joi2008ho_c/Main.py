import bisect
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

ref = set(arr)
for i in range(len(arr)):
    for j in range(len(arr)):
        ref.add(arr[i]+arr[j])
arr = sorted(list(ref))

ans = 0
for idx, num in enumerate(arr):
    res = m - num
    r_pos = bisect.bisect_right(arr, res)
    if r_pos > 0:
        r_pos -= 1
    if arr[r_pos]+num <= m:
        ans = max(ans, arr[r_pos]+num)

print(ans)