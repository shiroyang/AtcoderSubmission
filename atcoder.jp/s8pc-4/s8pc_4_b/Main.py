from itertools import combinations
n, k = map(int, input().split())
arr = list(map(int, input().split()))
ls = [i for i in range(1, n)]
ans = 10**16

def is_legal(selected):
    lowest = arr[0] 
    for idx, height in enumerate(arr):
        if idx in selected:
            lowest = arr[idx]
        else:
            if lowest < height:
                return False
    return True

for kumi in combinations(ls, k-1):
    cur = arr[0]
    tmp = 0
    selected = {0}
    for item in kumi:
        selected.add(item)
    for idx, height_idx in enumerate(kumi):
        height = arr[height_idx]
        if height > cur:
            cur = height
        else:
            tmp += cur + 1 - height
            cur += 1
    if is_legal(selected):
        ans = min(ans, tmp)

print(ans)
