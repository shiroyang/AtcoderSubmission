n = int(input())
s = input()
stride = 3
cnt = 0

for i in range(len(s)-stride+1):
    if s[i:i+3] == 'ABC':
        cnt += 1
print(cnt)