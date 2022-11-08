from math import sqrt

def check_prime(x):
    for i in range(2, round(sqrt(x))+1):
        if x % i == 0:
            return False
    return True

x = int(input())
if check_prime(x):
    print(x)
    exit()
    
while not check_prime(x):
    x += 1
    
print(x)