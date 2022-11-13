s = input()
arr = []
ans = 10**16
for i in s:
    arr.append(i)
stride = 2
for i in range(len(s)-stride):
    num = ''
    for j in range(3):
        num += arr[i+j]
    num = int(num)
    ans = min(ans, abs(num-753))
    
print(ans)