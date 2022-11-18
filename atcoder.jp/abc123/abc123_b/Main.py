def find_min(arr):
    bias = 10
    for i in range(len(arr)):
        tmp = arr[i] % 10
        if tmp == 0:
            tmp = 10
        if tmp < bias:
            bias = tmp
    return 10-bias


arr = [0]*5
for i in range(5):
    arr[i] = int(input())
bias = find_min(arr)
ans = 0
for i in range(5):
    if arr[i] % 10 == 0:
        ans += arr[i]
    else:
        ans += (arr[i] // 10 + 1)*10
print(ans - bias)