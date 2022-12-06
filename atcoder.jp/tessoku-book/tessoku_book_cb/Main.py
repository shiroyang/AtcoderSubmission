from itertools import combinations
n = int(input())
arr = list(map(int, input().split()))

for kumi in combinations(arr, 3):
    if kumi[0]+kumi[1]+kumi[2] == 1000:
        print("Yes")
        exit()
print("No")