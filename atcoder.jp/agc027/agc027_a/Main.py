# greedy
from itertools import accumulate
import bisect
n, x, = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr)
arr = list(accumulate(arr))
arr.append(x)
arr = sorted(arr)

pos = bisect.bisect_left(arr, x)
if pos == len(arr) - 1:
    if arr[pos] == arr[pos-1]:
        print(pos)
    else:
        print(pos-1)
    exit()
if arr[pos] == arr[pos+1]:
    print(pos+1)
else:
    print(pos)
