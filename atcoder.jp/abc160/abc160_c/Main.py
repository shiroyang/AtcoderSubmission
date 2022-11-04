k, n = map(int, input().split())
arr = list(map(int, input().split()))
interval = []
for i in range(0, len(arr)-1):
    interval.append(arr[i+1] - arr[i])
interval.append(k - arr[-1] + arr[0])
max_interval = max(interval[i] for i in range(len(interval)))
total = sum(interval[i] for i in range(len(interval)))
print(total - max_interval)
