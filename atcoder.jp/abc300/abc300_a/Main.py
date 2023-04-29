n, a, b= map(int, input().split())
ans = a+b
A = list(map(int, input().split()))
for i in range(n):
    if A[i] == ans:
        print(i+1)
        exit()