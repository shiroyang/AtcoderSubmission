import bisect

n, m ,x = map(int, input().split())
arr = list(map(int, input().split()))
arr.append(x)
arr.sort()
pos = bisect.bisect_left(arr, x)

print(min(pos, len(arr)-pos-1))