s = input()
for letter in s:
    print(chr(ord(letter) - (97-65)), end='')
print()