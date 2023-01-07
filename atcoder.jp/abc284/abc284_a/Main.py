n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
arr = arr[::-1]
for item in arr:
    print(item)