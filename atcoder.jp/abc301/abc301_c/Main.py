from collections import defaultdict

s = input()
t = input()
if len(s) != len(t):
    exit(print("No"))

d1 = defaultdict(int)
d2 = defaultdict(int)

for l in s:
    d1[l] +=1
    
for l in t:
    d2[l] += 1
    
for letter, num in d1.items():
    if letter == '@': continue
    tmp = d2[letter]
    if tmp >= num:
        d2[letter] -= num
        d1[letter] -= num

for letter, num in d1.items():
    if letter == '@': continue
    if letter not in ['a', 't', 'c', 'o', 'd', 'e', 'r']:continue
    stock = d2['@']
    consume = d1[letter]
    if consume > stock:
        exit(print("No"))
    else:
        d1[letter] = 0
        stock -= consume
        d2['@'] = stock

for letter, num in d2.items():
    if letter == '@': continue
    if letter not in ['a', 't', 'c', 'o', 'd', 'e', 'r']:continue
    stock = d1['@']
    consume = d2[letter]
    if consume > stock:
        exit(print("No"))
    else:
        d2[letter] = 0
        stock -= consume
        d1['@'] = stock

for item, val in d1.items():
    if item == '@': continue
    if d1[item] !=0: exit(print("No"))

stock1 = d1['@']
stock2 = d2['@']
if stock1 == stock2:
    exit(print("Yes"))
else:
    print("No")