import heapq

n = int(input())
h = []
for _ in range(n):
    s = input()
    if s[0] == '1':
        num, price = s.split()
        price = int(price)
        heapq.heappush(h, price)
    elif s[0] == '2':
        print(h[0])
    else:
        heapq.heappop(h)