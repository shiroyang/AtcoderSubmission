from collections import deque
n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr = deque(arr)
for i in range(k):
    arr.popleft()
    arr.append(0)
for i in arr:
    print(i, end = " ")
print()