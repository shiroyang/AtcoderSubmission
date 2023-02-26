from collections import deque
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
arr = deque(arr)

for i in range(n):
    arr.pop()
    arr.popleft()

print(sum(arr)/len(arr))