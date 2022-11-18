s = input()
ref = set()
for i in range(97, 97+26):
    ref.add(chr(i))
ref = sorted(ref)
for letter in s:
    if letter in ref:
        ref.remove(letter)
if len(ref) > 0:
    print(ref[0])
else:
    print("None")