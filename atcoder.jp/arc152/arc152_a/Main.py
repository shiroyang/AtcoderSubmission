import heapq

n, l = map(int, input().split())
arr = list(map(int, input().split()))
h = [-1*l]
heapq.heapify(h)
for idx, num in enumerate(arr):
    tmp = -1 * heapq.heappop(h)
    if tmp < num:
        print("No")
        exit()
    else:
        if tmp == num:
            pass
        else:
            l = 1
            r = tmp - num - 1
            heapq.heappush(h, -1*l)
            if r > 0:
                heapq.heappush(h, -1*r)
print("Yes")