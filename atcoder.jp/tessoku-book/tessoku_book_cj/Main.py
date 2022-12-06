import bisect
n = int(input())
arr = list(map(int, input().split()))
q = int(input())
arr.sort()
for _ in range(q):
    x = int(input())
    print(bisect.bisect_left(arr, x))