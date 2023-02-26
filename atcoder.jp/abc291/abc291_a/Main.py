s = input()
for idx, letter in enumerate(s, 1):
    if 'A' <= letter <= 'Z':
        print(idx)
        exit()