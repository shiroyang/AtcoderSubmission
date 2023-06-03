n = input()
l = len(n)
n = int(n)
if l < 3:
    exit(print(n))
    
n = int(n/(10**(l-3)))* (10**(l-3))
print(n)