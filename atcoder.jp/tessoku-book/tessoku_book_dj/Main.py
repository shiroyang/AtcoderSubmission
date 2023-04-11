# 桁DPみたいな考察

# 各桁の出現回数を記録する
counter = [0]*10

N = int(input())
s = str(N)[::-1]
L = len(str(N))

# 各桁: 一、十、百...
for i in range(L):
    # 既出、処理中、未出の場合分け
    digit = int(s[i])
    # 出現回数の記録
    for j in range(1, 10):
        # 既出
        if j < digit:
            tmp = ((N // 10**(i+1))+1)* (10**i)
            counter[j] += tmp
        elif j == digit:
            tmp = (N // 10**(i+1))*(10**i) + (N % (10**i)) + 1
            counter[j] += tmp
        else:
            tmp = (N // 10**(i+1)) * (10**i)
            counter[j] += tmp

ans = 0
for i in range(1, 10):
    ans += counter[i]*i

print(ans)