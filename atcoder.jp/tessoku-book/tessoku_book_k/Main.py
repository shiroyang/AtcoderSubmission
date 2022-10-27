def binary_search(arr, l, r, x):
    # base_check
    while(l <= r):
        mid = (l+r) // 2
        if arr[mid] == x:
            return mid+1
        elif arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1

n, x = map(int, input().split())
arr = list(map(int, input().split()))
print(binary_search(arr, 0, n-1, x))