a = 'abcdefghijklmnopqrstuvwxyz'
s = input()
[print(s.find(x), sep='') for x in a]


# print(' '.join(str(x) for x in [s.find(x) for x in a]))