n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr = list(dict.fromkeys(arr))
print(len(arr))