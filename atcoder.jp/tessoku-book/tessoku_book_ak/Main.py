n, m ,b = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = n*m*b + sum(A)*m + sum(C)*n
print(ans)