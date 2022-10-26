dd = [0]*100010
sum = []
d = int(input())
n = int(input())
for i in range(n):
    l,r = map(int, input().split())
    dd[l] += 1
    dd[r+1] -= 1
sum.append(0)
for i in range(1, d+1):
    sum.append(sum[i-1] + dd[i])
sum.pop(0)
for i in sum:
    print(i)