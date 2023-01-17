s = input().upper()
b = set(s)
l = [s.count(i) for i in b]
print('?' if l.count(max(l)) >= 2 else max([[s.count(v), v] for v in b])[1])