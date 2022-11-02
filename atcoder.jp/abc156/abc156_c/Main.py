n = int(input())
arr = list(map(int, input().split()))
m = round(sum(arr) / n)
err = 0
for item in arr:
    err += (item-m)**2
    
print(err)