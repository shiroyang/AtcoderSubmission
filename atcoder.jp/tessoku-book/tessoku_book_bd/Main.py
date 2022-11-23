n, q = map(int, input().split())
s = input()

MOD = 19971101
B = 101

h = [0]
# hash table index stars from 1
for i in range(n):
    h.append((h[-1]*B + ord(s[i])) % MOD) 

for i in range(q):
    a, b, c, d = map(int, input().split())
    # Be careful about the parenthesis
    hash1 = ((h[b] - h[a-1]*pow(B, b-a+1, MOD)) % MOD)
    hash2 = ((h[d] - h[c-1]*pow(B, d-c+1, MOD)) % MOD)
    if hash1 == hash2:
        print("Yes")
    else:
        print("No")