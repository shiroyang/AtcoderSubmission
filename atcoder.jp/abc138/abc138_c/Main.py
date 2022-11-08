import heapq

n = int(input())
arr = list(map(int, input().split()))
weight = 0
heapq.heapify(arr)

while (len(arr) >= 2):
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    heapq.heappush(arr, (a+b)/2)
print(heapq.heappop(arr))

