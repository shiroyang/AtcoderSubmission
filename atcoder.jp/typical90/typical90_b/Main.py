# 2**20 = 10**6
# 0 -> (
    
def is_ok(A):
    tmp = 0
    for item in A:
        if item == 0:
            tmp += 1
        else:
            tmp -= 1
        if tmp < 0:
            return False
        
    if tmp == 0:
        return True
    else: return False
        


N = int(input())
if N % 2 != 0: exit()

for i in range(1<<N):
    A = []
    for j in range(N):
        A.append((i>>j) & 1)  
    A = A[::-1]
    if is_ok(A):
        for k in range(len(A)):
            if A[k] == 0:
                print('(', end= '')
            else: print(')', end='')
        print()