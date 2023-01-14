def freq(d):
    return {v: d.count(v) for v in set(d)}


d = [int(x) for x in input().split()]
f = freq(d)
n = len(f)
print(d[0] * 1000 + 10000 if n == 1 else max(f, key=f.get) * 100 + 1000 if n == 2 else max(d) * 100)