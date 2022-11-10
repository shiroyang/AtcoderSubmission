from math import sqrt

def check_prime(x):    
    if x % 2 == 0:
        if x == 2:
            return True
        else:
            return False
    for i in range(3, round(sqrt(x))+1, 2):
        if x % i == 0:
            return False
    return True

n = int(input())
for i in range(n):
    x = int(input())
    if check_prime(x):
        print("Yes")
    else:
        print("No")