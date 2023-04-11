from itertools import combinations
N = int(input())

A = [3, 5, 7]
cnt = 0

for i in range(1, len(A)+1):
    ls = list(combinations(A, i))
    bit = i % 2

    for comb in ls:
        m = 1
        for item in comb:
            m *= item
        cnt = cnt + (2*bit-1)* (N // m)
    
print(cnt)