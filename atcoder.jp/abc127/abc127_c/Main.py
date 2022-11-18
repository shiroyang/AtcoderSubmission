lower_bound = 0
upper_bound = 10**8
n, m = map(int, input().split())
for _ in range(m):
    l, r = map(int, input().split())
    lower_bound = max(lower_bound, l)
    upper_bound = min(upper_bound, r)

if (upper_bound - lower_bound >= 0):
    print(upper_bound - lower_bound + 1)
else:
    print("0")