from math import ceil

h, w = map(int, input().split())
if h == 1 or w == 1:
    print("1")
    exit()
print(ceil(h*w/2))