n = int(input())
arr = list(map(int, input().split()))
cnt = 0
flag = True

while flag:
    for index, item in enumerate(arr):
        if item % 2 == 0:
            arr[index] = item / 2
        else:
            flag = False
    cnt += 1
cnt -= 1

print(cnt)