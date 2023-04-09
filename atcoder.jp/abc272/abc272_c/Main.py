# even + even or odd + odd
N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)

Odd = []
Even = []

for item in A:
    if item % 2 == 0:
        Even.append(item)
    else:
        Odd.append(item)
        
ans = -1
if len(Even) >= 2:
    ans = max(ans, Even[0]+Even[1])
if len(Odd) >= 2:
    ans = max(ans, Odd[0]+Odd[1])
    
print(ans)