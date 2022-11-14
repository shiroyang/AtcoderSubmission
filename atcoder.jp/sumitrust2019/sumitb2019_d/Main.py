# O(n)
def search(s, num):
    cnt = 0
    for i in range(len(s)):
        if s[i] in num[cnt]:
            cnt += 1
        if cnt == 3:
            return True
    return False


n = int(input())
s = input()
ans = 0
# 换个枚举的思路
for i in range(10):
    for j in range(10):
        for k in range(10):
            num = str(i)+str(j)+str(k)
            if(search(s, num)):
                ans += 1
print(ans)