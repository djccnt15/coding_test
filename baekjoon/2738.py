def add(*a):
    return [[sum(v) for v in zip(*i)] for i in zip(*a)]


m, n = (int(x) for x in input().split())
a, b = ([[int(n) for n in input().split()] for _ in range(m)] for _ in range(2))
[print(v) for r in add(a, b) for v in r]