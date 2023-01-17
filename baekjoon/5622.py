d = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
s = input()
print(sum(d.index(b) + 3 for a in s for b in d if b.find(a) >= 0))