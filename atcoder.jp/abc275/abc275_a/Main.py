n = int(input())
arr = list(map(int, input().split()))

max = 0
for i in arr:
    if max < i:
        max = i

for index, item in enumerate(arr):
    if max == item:
        print(index+1)
        exit()