# catupper様の写経
# stack内にはindexのみ記録

stack = []
N = int(input())
A = list(map(int, input().split()))

ans = []

for i in range(len(A)):
    # スタック内を単調に減少させる
    while stack and A[stack[-1]] <= A[i]:
        stack.pop()
    if stack:
        ans.append(stack[-1] + 1)
    else:
        ans.append(-1)
    stack.append(i)

print(*ans)