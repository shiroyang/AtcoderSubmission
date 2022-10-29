n = int(input())
arr = list(map(int, input().split()))

arr.sort()
sum_a = 0
sum_b = 0
while len(arr)>=2:
    sum_a += arr.pop()
    sum_b += arr.pop()

if len(arr) == 1:
    sum_a += arr.pop()

print(sum_a - sum_b)