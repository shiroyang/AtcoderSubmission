Mat = []
for _ in range(8):
    Mat.append(list(input().split()))

for i, line in enumerate(Mat):
    for j, letter in enumerate(line):
        if letter.find('*')!= -1:
            buma = letter.find('*')
            ans = chr(97 + buma)
            ans += str(8 - i)
            print(ans)