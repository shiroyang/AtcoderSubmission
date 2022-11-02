cnt = 0
num = 0
a, b = map(int, input().split())

if b == 1:
    print("0")
    exit()

while num < b:
    cnt += 1
    if (cnt == 1):
        num += a
    else:
        num += a - 1
        
print(cnt)