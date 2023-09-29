a = 'abcdefghijklmnopqrstuvwxyz'
s = input()
print(*[s.find(x) for x in a])