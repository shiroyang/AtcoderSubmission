# 草の高さの最小値を求める
# 前から”＜”だけを処理し、後ろから”>”だけを処理する

N = int(input())
s = input()

A = [0]*(N)
B = [0]*(N)

streak1 = 1; A[0] = 1
for i in range(len(s)):
    if s[i] == 'A':
        streak1 += 1
    else:
        streak1 = 1
    A[i+1] = streak1

streak2 = 1; B[len(s)] = 1
for i in range(len(s)-1, -1, -1):
    if s[i] == 'B':
        streak2 += 1
    else:
        streak2 = 1
    B[i] = streak2

ans = 0
for i in range(N):
    ans += max(A[i], B[i])

print(ans)