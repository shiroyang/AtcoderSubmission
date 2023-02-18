from collections import deque

ans = deque()

def solve(x):
    s = str(x)
    arr = []
    cnt = 0
    
    for idx, ele in enumerate(s):
        if ele == '1':
            cnt += 1
            arr.append(idx)

    
    if cnt == 0:
        return 0

    elif cnt % 2 == 1:
        return -1
    
    elif cnt == 2:
        if s == '11' or s == '011' or s == '110':
            return -1
        
        elif s == '0110':
            return 3
        
        elif arr[1] - arr[0] >= 2:
            return 1
        else:
            return 2
    else:
        return (cnt // 2)


'''
n = 7
for i in range(1<<n):
    x = bin(i)[2:]
    print(x)
    print(solve(x))
    print()
'''



t = int(input())
for _ in range(t):
    _ = input()
    s = input()
    ans.append(solve(s))
    
while len(ans) > 0:
    print(ans.popleft())
