n = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(list(set(arr)))

ref = {}
idx = 1

for item in sorted_arr:
    if ref.get(item ,-1) == -1:
        ref[item] = idx
        idx += 1
        
for item in arr:
    print(ref[item], end=" ")
print()