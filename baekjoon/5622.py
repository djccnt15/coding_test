d = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
print(sum(d.index(b) + 3 for a in input() for b in d if b.find(a) >= 0))