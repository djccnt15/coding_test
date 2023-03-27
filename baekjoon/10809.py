a = 'abcdefghijklmnopqrstuvwxyz'
s = input()
for x in a:
    print(s.find(x), sep='')


# print(' '.join(str(x) for x in [s.find(x) for x in a]))