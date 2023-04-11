# 常にニム和をゼロにすると最後の石を取れる

n, h, w = map(int, input().split())
AB = [map(lambda x: int(x)-1, input().split()) for _ in range(n)]
A, B = map(list, zip(*AB))

nim_sum = 0
for item in A:
    nim_sum ^= item
for item in B:
    nim_sum ^= item
    
if nim_sum == 0:
    print("Second")
else:
    print("First")
