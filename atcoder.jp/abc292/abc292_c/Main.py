# 半分全列挙
# let X = AB, Y = N-X = CD
# Assume A <= B
n = int(input())
ans = 0

# O(n)
for x in range(1, n):
    y = n - x
    
    cnt_x = 0
    cnt_y = 0
    
    i = 1
    while i*i <= x:
        if x % i == 0:
            cnt_x += 1
            if i*i != x:
                cnt_x += 1
        i += 1        
                
    j = 1
    while j*j <= y:
        if y % j == 0:
            cnt_y += 1
            if j*j != y:
                cnt_y += 1
        j += 1
    
    ans += cnt_x * cnt_y
    
print(ans)