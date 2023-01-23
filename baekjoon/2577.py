a, b, c = (int(x) for x in (input() for _ in range(3)))
d = list(str(a * b * c))
[print(d.count(str(i))) for i in range(10)]