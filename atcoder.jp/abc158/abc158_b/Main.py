n, a, b = map(int, input().split())

div = n//(a+b)
rem_a = min(n - div*(a+b), a)
print(div*a + rem_a)
    
