n ,t = map(int, input().split())
arr = list(map(int, input().split()))
s = sum(arr)

if t >= s:
    t %= s
    
for idx, num in enumerate(arr, 1):
    if t >= num:
        t -= num
    else:
        print(idx, t)
        exit()