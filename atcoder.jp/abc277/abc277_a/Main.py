n, x = map(int, input().split())
arr = list(map(int, input().split()))
for idx, item in enumerate(arr):
    if item == x:
        print(idx+1)
