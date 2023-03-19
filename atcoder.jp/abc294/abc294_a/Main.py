n = int(input())
arr = list(map(int, input().split()))
for ele in arr:
    if ele % 2 == 0:
        print(ele, end=' ')
print()