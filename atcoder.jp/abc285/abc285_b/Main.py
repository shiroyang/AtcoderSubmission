# O(N^2)

n = int(input())
s = input()

for i in range(1, n):
    l = 0
    r = l + i
    while r < n and s[l] != s[r]:
        l += 1
        r += 1
    print(l)