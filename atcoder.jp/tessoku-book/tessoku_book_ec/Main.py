# String Hash
# Hash Table starts from 0 as 累積和
# IMPORTANT!
import sys
input = lambda: sys.stdin.readline()[:-1]

def struct_hash(s):
    A = [0]
    for item in s:
        nxt = (A[-1]*DIGIT + (ord(item)-97)) % MOD
        A.append(nxt)
    return A

def get_hash_val(A, l ,r):
    hash_val = (A[r] - (A[l-1] * pow(DIGIT, r-l+1, MOD))%MOD)%MOD
    return hash_val

MOD = 10**9+7
DIGIT = 26
N, Q = map(int, input().split())
s = input()
sr = s[::-1]
H = []
HR = []

H = struct_hash(s)
HR = struct_hash(sr)

for _ in range(Q):
    l, r = map(int, input().split())
    
    if get_hash_val(H, l, r) == get_hash_val(HR, N+1-r, N+1-l):
        print("Yes")
    else:
        print("No")