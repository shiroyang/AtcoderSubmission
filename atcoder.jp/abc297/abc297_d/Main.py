# After Contest
# 左右に引くのが、gcdに似ている！
# 

ans = 0
a, b = map(int, input().split())

if a < b: a, b = b, a
cnt = 0

while b != 0:
    cnt += a // b
    a, b = b, a % b  
      
print(cnt-1)