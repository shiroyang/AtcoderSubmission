t = int(input())
n = int(input())
arr = [0]*(t+1)
for _ in range(n):
    l, r = map(int, input().split())
    arr[l]+= 1
    arr[r]-= 1
ans = [arr[0]]
for i in range(1, t+1):
    ans.append(ans[-1]+arr[i])
for i in range(t):
    print(ans[i])