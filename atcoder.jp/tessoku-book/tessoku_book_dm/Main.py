# Record num % 100

d = [0]*100

N = int(input())
A = list(map(int, input().split()))

for item in A:
    d[item%100] += 1

cnt = 0
# rem1 <-> rem 99
# rem0 <-> rem 0 and rem50 <-> rem50
# 2Cn = n(n-1)//2
for i in range(1, 50):
    j = 100 - i    
    cnt += d[i] * d[j] 
    
cnt += d[0]*(d[0]-1)//2
cnt += d[50]*(d[50]-1)//2

print(cnt)