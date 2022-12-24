n = int(input())
arr = [0]+list(map(int, input().split()))
q = int(input())
for _ in range(q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        arr[s[1]] = s[2]
    elif s[0] == 2:
        print(arr[s[1]])