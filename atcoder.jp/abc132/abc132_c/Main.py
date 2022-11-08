n = int(input())

arr = list(map(int, input().split()))
if (len(arr) % 2 == 1):
    print("0")
    exit()
arr.sort()
l = arr[len(arr)//2 -1]
r = arr[len(arr)//2]

if l == r:
    print("0")
else:
    print(r-l)
