from itertools import permutations

idx1, idx2 = 0, 0
n = int(input())
arr = [i for i in range(1,n+1)]
ref1 = tuple(map(int, input().split()))
ref2 = tuple(map(int, input().split()))
for idx, arragement in enumerate(permutations(arr)):
    if arragement == ref1:
        idx1 = idx
    if arragement == ref2:
        idx2 = idx
print(abs(idx1-idx2))

