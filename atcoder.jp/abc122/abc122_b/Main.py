s = input()
ans = 0

for i in range(len(s)):
    if s[i] in 'ATGC':
        j = i
        while j<=len(s)-1 and s[j] in 'ATGC':
            j += 1
        ans = max(ans, j-i)
      
print(ans)     
