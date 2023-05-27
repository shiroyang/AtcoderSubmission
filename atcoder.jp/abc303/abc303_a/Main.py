N = int(input())
S = input()
T = input()

for i in range(N):
    if S[i] == T[i]:
        continue
    elif S[i] == '1' and T[i] == 'l':
        continue
    elif S[i] == 'l' and T[i] == '1':
        continue
    elif S[i] == 'o' and T[i] == '0':
        continue
    elif S[i] == '0' and T[i] == 'o':
        continue
    exit(print("No"))

print("Yes")    