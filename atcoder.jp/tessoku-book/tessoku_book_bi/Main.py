n, m = map(int, input().split())
Mat = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    Mat[u].append(v)
    Mat[v].append(u)

for i in range(1, n+1):
    Mat[i].sort()

for i in range(1, n+1):
    output = str(i)
    output += ': {'
    output += ', '.join(map(str, Mat[i]))
    output += '}'
    print(output)
    


