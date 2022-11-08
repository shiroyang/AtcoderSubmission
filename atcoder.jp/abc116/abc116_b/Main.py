import time

start = time.time()
n = int(input())
cnt = 1
ref = {}
ref[n] = cnt
while True:
    if (n % 2 == 0):
        n = round(n / 2)
    else:
        n = 3*n + 1
    cnt += 1
    if ref.get(n, -1) == -1:
        ref[n] = cnt
    else:
        print(cnt)
        exit()
        
print("-1")
